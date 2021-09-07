from django.db import models

# Create your models here.

class Campania(models.Model):
    codigo = models.CharField(max_length=10)
    linea = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return '{} {}'.format(self.codigo, self.nombre)
