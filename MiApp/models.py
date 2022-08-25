from django.db import models

# Create your models here.
class Familia(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    mail = models.EmailField()
    nacionalidad = models.CharField(max_length=40)
    genero = models.CharField(max_length=15)
    relacion = models.CharField(max_length=40)
    mascotas = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now=True)
