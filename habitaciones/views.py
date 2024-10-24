from django.shortcuts import render
from .models import Habitacion

from django.shortcuts import render
from .models import Habitacion

def consulta_habitaciones(request):
    habitaciones = []
    numeros_habitaciones = ""
    
    if request.method == 'POST':
        tipo_habitacion = request.POST.get('tipo_habitacion')
        habitaciones = Habitacion.objects.filter(tipo_habitacion__iexact=tipo_habitacion, disponible=True)
        numeros_habitaciones = ", ".join([str(h.numero_habitacion) for h in habitaciones])

    return render(request, 'index.html', {
        'habitaciones_form_1': habitaciones,
        'numeros_habitaciones_form_1': numeros_habitaciones
    })

from django.http import JsonResponse
from .models import Habitacion

def obtener_precio_habitacion(request):
    tipo_habitacion = request.GET.get('tipo_habitacion')
    try:
        habitacion = Habitacion.objects.get(tipo_habitacion=tipo_habitacion, disponible=True)
        return JsonResponse({'precio': habitacion.precio_habitacion})
    except Habitacion.DoesNotExist:
        return JsonResponse({'precio': 0}) 
    
    
from django.shortcuts import render
from django.http import JsonResponse

def obtener_habitaciones_disponibles(request):
    tipo_habitacion = ''
    cantidad_habitaciones = ''
    numeros_habitaciones_asignadas = ""

    if request.method == 'POST':
        tipo_habitacion = request.POST.get('tipo_habitacion_consulta', '')
        cantidad_habitaciones = request.POST.get('cantidad_habitaciones_consulta', '')

        if tipo_habitacion and cantidad_habitaciones and cantidad_habitaciones.isnumeric() and int(cantidad_habitaciones) > 0:
            cantidad_habitaciones = int(cantidad_habitaciones)
            habitaciones_disponibles = Habitacion.objects.filter(
                tipo_habitacion__iexact=tipo_habitacion, disponible=True
            )[:cantidad_habitaciones]
            numeros_habitaciones_asignadas = ", ".join([str(h.numero_habitacion) for h in habitaciones_disponibles])

        return JsonResponse({'numeros_habitaciones_asignadas': numeros_habitaciones_asignadas})

    return render(request, 'index.html', {
        'tipo_habitacion': tipo_habitacion,
        'cantidad_habitaciones': cantidad_habitaciones,
        'numeros_habitaciones_asignadas': numeros_habitaciones_asignadas,
    })













