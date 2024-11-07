from django.shortcuts import render
from .models import ServicioExtra  
from reserva.models import Reserva
from django.http import JsonResponse

def servicios_extra(request):
    servicios = ServicioExtra.objects.all()  
    return render(request, 'servicio.html', {'servicios': servicios}) 

def consulta(request):
 
    clientes = Reserva.objects.all().values('nombre_cliente', 'cedula', 'numero_habitaciones_asignadas')

    return JsonResponse(list(clientes), safe=False)