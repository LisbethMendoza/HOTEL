from django.db import models

# reserva/models.py
class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    cedula = models.CharField(max_length=13, default="9999999999999")  
    cantidad_personas = models.PositiveIntegerField()
    cantidad_habitaciones_reservar = models.PositiveIntegerField()
    tipo_habitacion = models.CharField(max_length=20)
    numero_habitaciones_asignadas = models.TextField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    total_pago = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default="Activa")

    def __str__(self):
        return f"Reserva de {self.nombre_cliente} para {self.cantidad_personas} personas"

