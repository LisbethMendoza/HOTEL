# Generated by Django 5.1.1 on 2024-11-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_alter_reserva_cedula'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='estado',
            field=models.CharField(default='Activa', max_length=20),
        ),
    ]
