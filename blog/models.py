from unittest.util import _MAX_LENGTH
from urllib import request
from django.db import models

# Create your models here.
class autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)

class articulo(models.Model):
    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null = True)

class seccion(models.Model):
    nombre = models.CharField(max_length=30)
    