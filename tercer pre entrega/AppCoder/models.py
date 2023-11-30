from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.camada}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    porfesion = models.CharField(max_length=40)

class Entregable(models.Model):
    
    nombre =models.CharField(max_length=40)
    fechaDeEntrega =models.DateField()
    entregado = models.BooleanField()

class Libro(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    numerodeguardado = models.IntegerField()