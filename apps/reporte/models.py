from django.db import models
from apps.persona.models import Persona
from apps.campania.models import Campania
from apps.actividad.models import Actividad
from django.contrib.auth.models import User
# Create your models here.

class Reporte (models.Model):
    fecha = models.DateField()
    descripcion = models.TextField()
    horas = models.DecimalField(max_digits= 7, decimal_places=3)
    persona = models.ForeignKey (Persona, null=True, blank=True, on_delete=models.CASCADE)
    campania = models.ForeignKey (Campania, null=True, blank=True, on_delete=models.CASCADE)
    actividad = models.ForeignKey (Actividad, null=True, blank=True, on_delete=models.CASCADE)
    usuario = models.ForeignKey (User, null=True, blank=True, on_delete=models.CASCADE)

