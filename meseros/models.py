from django.db import models

# Create your models here.
class Meseros(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField(max_length=2)
    pais = models.CharField(max_length=40)
