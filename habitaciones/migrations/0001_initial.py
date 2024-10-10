# Generated by Django 5.1.1 on 2024-10-10 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_habitacion', models.CharField(max_length=50)),
                ('precio_habitacion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numero_habitacion', models.CharField(max_length=10)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
    ]