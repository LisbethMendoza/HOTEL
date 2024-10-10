from django.shortcuts import render
from .models import Habitacion

def consulta_habitaciones_view(request):
    habitaciones = None
    if request.method == 'POST':
        tipo_habitacion = request.POST.get('tipo_habitacion')
        habitaciones = Habitacion.objects.filter(tipo_habitacion=tipo_habitacion, disponible=True)
    
    return render(request, 'consulta.html', {'habitaciones': habitaciones})
