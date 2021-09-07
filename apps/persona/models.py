from django.db import models
from django.db.models.base import Model

# Create your models here.

class Persona (models.Model):
    nombre = models.CharField (max_length=50)
    apellidos = models.CharField(max_length=70)
    masivo = models.CharField(max_length=50)
    cargo = models.CharField(max_length=70)
    horas_total = models.IntegerField ()
    porc_establecido = models.IntegerField()

    def __str__(self) -> str:
        return '{} {}'.format(self.nombre, self.apellidos)
