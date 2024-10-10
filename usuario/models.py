from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)  
    contrasena = models.CharField(max_length=128, null=True)  

    def __str__(self):
        return self.nombre  
