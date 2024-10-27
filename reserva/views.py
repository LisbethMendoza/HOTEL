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
        # Obtener datos del formulario
        nombre_cliente = request.POST.get('nombre_cliente')
        cantidad_personas = request.POST.get('cantidad_personas')
        cantidad_habitaciones_reservar = request.POST.get('cantidad_habitaciones_consulta')
        tipo_habitacion = request.POST.get('tipo_habitacion_consulta')
        numero_habitaciones_asignadas = request.POST.get('numero_habitaciones_consulta')
        fecha_entrada = request.POST.get('fecha_entrada')
        fecha_salida = request.POST.get('fecha_salida')
        total_pago = request.POST.get('total_pago')

        # Crear una nueva reserva
        nueva_reserva = Reserva(
            nombre_cliente=nombre_cliente,
            cantidad_personas=cantidad_personas,
            cantidad_habitaciones_reservar=cantidad_habitaciones_reservar,
            tipo_habitacion=tipo_habitacion,
            numero_habitaciones_asignadas=numero_habitaciones_asignadas,
            fecha_entrada=fecha_entrada,
            fecha_salida=fecha_salida,
            total_pago=total_pago,
        )
        nueva_reserva.save()  # Guardar la reserva en la base de datos

        return redirect('index')  # Redirige de vuelta al formulario (index.html)

    return render(request, 'index.html')  # Renderizar el formulario en caso de que no sea POST
def index(request):
    reservas = Reserva.objects.all()  # Obtener todas las reservas, si necesitas mostrar algo
    return render(request, 'index.html', {'reservas': reservas}) 
