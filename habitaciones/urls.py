from django.urls import path
from .views import consulta_habitaciones, obtener_precio_habitacion, obtener_habitaciones_disponibles


urlpatterns = [
    path('consulta-habitaciones/', consulta_habitaciones, name='consulta_habitaciones'),
    path('obtener_precio/', obtener_precio_habitacion, name='obtener_precio_habitacion'),
    path('obtener_habitaciones_disponibles/', obtener_habitaciones_disponibles, name='obtener_habitaciones_disponibles'),
]

