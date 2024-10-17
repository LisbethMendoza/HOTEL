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
        'habitaciones': habitaciones,
        'numeros_habitaciones': numeros_habitaciones
    })
def index(request):
    return render(request, 'index.html')