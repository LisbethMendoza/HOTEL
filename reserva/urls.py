
from django.urls import path
from .views import calculo_total
from .views import insert, index


urlpatterns = [
      path('calculo_total/', calculo_total, name='calculo_total'),
      path('insert/', insert, name='insert'),  
      path('', index, name='index'),   
]
