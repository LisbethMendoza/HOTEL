from django.urls import path
from . import views  
import usuario.views

urlpatterns = [
    path('', views.login_view, name='login'),  
    path('index/', usuario.views.index_view, name='index'),  
]