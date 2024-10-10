from django.urls import path
from .views import consulta_habitaciones_view

urlpatterns = [
    path('consulta/', consulta_habitaciones_view, name='consulta_habitaciones'),
]
