from django.db import models

class Habitaciones(models.Model):
    tipo_habitacion = models.CharField(max_length=50)
    precio_habitacion = models.DecimalField(max_digits=10, decimal_places=2)
    numero_habitacion = models.CharField(max_length=10)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo_habitacion} - {self.numero_habitacion}"
