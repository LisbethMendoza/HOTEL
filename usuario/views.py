from django.shortcuts import render, redirect
from .models import Usuario
from reserva.models import Reserva
from django.http import JsonResponse
from django.utils import timezone


def updatesalida(request):
    today = timezone.now().date() 
    reservas_actualizadas = Reserva.objects.filter(fecha_salida__lte=today, estado="Activa").update(estado="Inactiva")
    return JsonResponse({'actualizadas': reservas_actualizadas})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        try:
            usuario = Usuario.objects.get(nombre=username)

            
            if usuario.contrasena == password:
                return redirect('index')  
            else:
                error = 'Nombre de usuario o contraseña incorrectos'
                return render(request, 'Login.html', {'error': error})
        except Usuario.DoesNotExist:
            error = 'Nombre de usuario o contraseña incorrectos'
            return render(request, 'Login.html', {'error': error})

    return render(request, 'Login.html')



def index_view(request):
    return render(request, 'index.html') 
