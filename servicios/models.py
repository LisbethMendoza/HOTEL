from django.db import models

class ServicioExtra(models.Model):
    servicio = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return f"Servicio: {self.servicio} - Precio: ${self.precio}"


