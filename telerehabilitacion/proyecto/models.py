from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.
class Ciudad(models.Model):
    ciudad = models.CharField(max_length=20)

    def __str__(self):
        return self.ciudad

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=15)
    a_paterno = models.CharField(max_length=15)
    a_materno = models.CharField(max_length=15)
    fecha_nacimiento =models.DateField()
    telefono = models.IntegerField()
    id_ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Kinesiologo(Usuario):
    
    def __str__(self):
        return self.nombre
class Familiar(Usuario):
    id_kinesiologo = models.ForeignKey(Kinesiologo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Paciente(Usuario):

    def __str__(self):
        return self.nombre

class Ejercicio(models.Model):
    nombre_ejercicio= models.CharField(max_length=30)
    detalle_ejercicio = models.TextField(max_length=150)
    fecha_ejercicio = models.DateTimeField(default=timezone.now)
    id_kinesiologo = models.ForeignKey(Kinesiologo, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_ejercicio

class Resultado(models.Model):
    comentarios = models.TextField(max_length=300)
    completado = models.CharField(max_length=1)
    evidencia = models.FileField(upload_to='video')
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.completado