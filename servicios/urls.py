# servicios/urls.py
from django.urls import path
from .views import servicios_extra, consulta 

urlpatterns = [
    path('', servicios_extra, name='servicios_extra'),
    path('consulta/', consulta, name='consulta'),  
]
