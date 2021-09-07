from django.db import models

# Create your models here.
class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return '{}'.format(self.nombre)