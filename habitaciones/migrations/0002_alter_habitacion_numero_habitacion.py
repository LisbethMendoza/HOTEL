# Generated by Django 5.1.1 on 2024-11-01 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='numero_habitacion',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
