# habitaciones/models.py
from django.db import models

class Habitacion(models.Model):
    TIPO_HABITACION_CHOICES = [
        ('simple', 'Simple'),
        ('doble', 'Doble'),
        ('suite', 'Suite'),
    ]
    
    tipo_habitacion = models.CharField(max_length=10, choices=TIPO_HABITACION_CHOICES)
    precio_habitacion = models.DecimalField(max_digits=10, decimal_places=2)
    numero_habitacion = models.IntegerField(unique=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo_habitacion} - {self.numero_habitacion}"

    class Meta:
        db_table = 'habitaciones_habitaciones' 
