from django.db import models
from servicios.models import ServicioExtra
from reserva.models import Reserva

class ReservaServicio(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    servicio_extra = models.ForeignKey(ServicioExtra, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva {self.reserva.nombre_cliente} - Servicio: {self.servicio_extra.servicio}"
