# Generated by Django 5.1.1 on 2024-10-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('cantidad_personas', models.PositiveIntegerField()),
                ('cantidad_habitaciones_reservar', models.PositiveIntegerField()),
                ('tipo_habitacion', models.CharField(max_length=20)),
                ('numero_habitaciones_asignadas', models.TextField()),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('total_pago', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]