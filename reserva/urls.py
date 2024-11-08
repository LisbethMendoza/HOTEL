
from django.urls import path
from .views import calculo_total
from .views import insert, index, consulta_reserva


urlpatterns = [
      path('calculo_total/', calculo_total, name='calculo_total'),
      path('insert/', insert, name='insert'),  
      path('', index, name='index'),   
       path('consulta_reserva/', consulta_reserva, name='consulta_reserva'),
       
]
