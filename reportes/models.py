from django.db import models

class Reporte(models.Model):
    hash = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    json = models.FileField(upload_to='uploads/')
