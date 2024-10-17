from django.urls import path
from .views import consulta_habitaciones

urlpatterns = [
    path('consulta-habitaciones/', consulta_habitaciones, name='consulta_habitaciones'),
]

