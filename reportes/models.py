from django.db import models
from django.utils import timezone

class Reporte(models.Model):
    hash = models.CharField(max_length=200)
    fecha = models.DateTimeField( auto_now_add=True)
    informacion = models.CharField(max_length=1048575,default='No hay informacion')

    def __str__(self):
        return self.title
