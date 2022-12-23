from django.db import models

# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=10)
    pais = models.CharField(max_length=25, default='')
