from django.db import models

# Create your models here.
class Menu(models.Model):
    nombre_menu = models.CharField(max_length=40)
    lista = models.CharField(max_length=20)
    ingredientes = models.CharField(max_length=12)