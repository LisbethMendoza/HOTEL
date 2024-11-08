from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from habitaciones.models import Habitacion

def calculo_total(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre_cliente')
        cantidad_personas = int(request.POST.get('cantidad_personas', 0))
        tipo_habitacion = request.POST.get('tipo_habitacion_consulta', '')
        cantidad_habitaciones = int(request.POST.get('cantidad_habitaciones_consulta', 0))
        fecha_entrada = request.POST.get('fecha_entrada')
        fecha_salida = request.POST.get('fecha_salida')

        try:
            
            fecha_entrada = timezone.datetime.strptime(fecha_entrada, '%Y-%m-%d')
            fecha_salida = timezone.datetime.strptime(fecha_salida, '%Y-%m-%d')
            cantidad_noches = (fecha_salida - fecha_entrada).days

            if cantidad_noches < 0:
                return JsonResponse({'error': 'La fecha de entrada debe ser anterior a la fecha de salida.'})

      
            habitacion = Habitacion.objects.filter(tipo_habitacion=tipo_habitacion).first()
            if not habitacion:
                return JsonResponse({'error': 'No se encontró una habitación disponible de este tipo.'})

            precio_por_noche = habitacion.precio_habitacion
            total_pago = cantidad_noches * precio_por_noche * cantidad_habitaciones

            return JsonResponse({'total_pago': total_pago})

        except ValueError:
            return JsonResponse({'error': 'Formato de fecha incorrecto. Use YYYY-MM-DD.'})

    return JsonResponse({'error': 'Solicitud no válida'}, status=400)




# reserva/views.py
from django.shortcuts import render, redirect
from .models import Reserva


def insert(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre_cliente')
        cantidad_personas = request.POST.get('cantidad_personas')
        cantidad_habitaciones_reservar = request.POST.get('cantidad_habitaciones_consulta')
        tipo_habitacion = request.POST.get('tipo_habitacion_consulta')
        numero_habitaciones_asignadas = request.POST.get('numero_habitaciones_consulta')
        fecha_entrada = request.POST.get('fecha_entrada')
        fecha_salida = request.POST.get('fecha_salida')
        total_pago = request.POST.get('total_pago')
        cedula = request.POST.get('cedula_cliente')

        nueva_reserva = Reserva(
            nombre_cliente=nombre_cliente,
            cantidad_personas=cantidad_personas,
            cantidad_habitaciones_reservar=cantidad_habitaciones_reservar,
            tipo_habitacion=tipo_habitacion,
            numero_habitaciones_asignadas=numero_habitaciones_asignadas,
            fecha_entrada=fecha_entrada,
            fecha_salida=fecha_salida,
            total_pago=total_pago,
            cedula=cedula,
        )
        nueva_reserva.save()

        habitaciones_asignadas = numero_habitaciones_asignadas.split(',')
        for habitacion_numero in habitaciones_asignadas:
            habitacion_numero = habitacion_numero.strip()  
            habitacion = Habitacion.objects.filter(numero_habitacion=habitacion_numero).first()
            if habitacion:
                habitacion.disponible = False
                habitacion.save()
                
        return redirect('index')


def index(request):
    reservas = Reserva.objects.all() 
    return render(request, 'index.html', {'reservas': reservas}) 




from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Reserva

def consulta_reserva(request):
    nombre_cliente = request.GET.get('nombre_cliente')
    cedula_cliente = request.GET.get('cedula_cliente')

    try:
        if nombre_cliente:
            reserva = Reserva.objects.get(nombre_cliente=nombre_cliente)
        elif cedula_cliente:
            reserva = Reserva.objects.get(cedula=cedula_cliente)
        else:
            return JsonResponse({'error': 'No se proporcionó nombre o cédula'}, status=400)

        reserva_data = {
            'nombre_cliente': reserva.nombre_cliente,
            'cedula': reserva.cedula,
            'cantidad_personas': reserva.cantidad_personas,
            'cantidad_habitaciones_reservar': reserva.cantidad_habitaciones_reservar,
            'tipo_habitacion': reserva.tipo_habitacion,
            'numero_habitaciones_asignadas': reserva.numero_habitaciones_asignadas,
            'fecha_entrada': reserva.fecha_entrada,
            'fecha_salida': reserva.fecha_salida,
            'total_pago': float(reserva.total_pago),
        }
        return JsonResponse(reserva_data)

    except Reserva.DoesNotExist:
        return JsonResponse({'error': 'No se encontró la reserva'}, status=404)
