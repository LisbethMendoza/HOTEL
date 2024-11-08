from django.urls import path
from .views import crear_reserva_servicio,actualizar_total_pago

urlpatterns = [
    path('crear_reserva_servicio/', crear_reserva_servicio, name='crear_reserva_servicio'),
    path('actualizar_total_pago/', actualizar_total_pago, name='actualizar_total_pago'),
    
]
