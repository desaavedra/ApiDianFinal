from django.db import models
from django.utils import timezone

class Reporte(models.Model):
    hash = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now=True, auto_now_add=True)
    json = models.CharField(max_length=2000000000)

    def __str__(self):
        return self.title
