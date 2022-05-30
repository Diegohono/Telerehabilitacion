from distutils.command.upload import upload
#from turtle import update
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.deletion import CASCADE
from django.utils import timezone
#from pandas.core.algorithms import mode

# Create your models here.       
class Usuario(models.Model):
    userD = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=15)
    rut = models.CharField(max_length=12)
    a_paterno = models.CharField(max_length=15)
    a_materno = models.CharField(max_length=15)
    fecha_nacimiento =models.DateField()
    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="", null=True)
    class Meta:
        abstract = True

class Kinesiologo(Usuario):
    def __str__(self):
        return self.nombre

class Paciente(Usuario):
    id_kinesiologo = models.ForeignKey(Kinesiologo, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Familiar(Usuario):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Ejercicio(models.Model):
    nombre_ejercicio= models.CharField(max_length=30)
    detalle_ejercicio = models.TextField(max_length=150)
    video = models.FileField(upload_to='', null=True)
    id_kinesiologo = models.ForeignKey(Kinesiologo, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_ejercicio

class Programa(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cantidad_semanas= models.IntegerField()
    def __str__(self):
        return self.paciente.nombre+'-'+str(self.cantidad_semanas)
    


class Asignar_ejercicio(models.Model):
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    fecha_ejercicio = models.DateField()
    semana = models.IntegerField()
    n_ejercicio= models.IntegerField()
    comentarios_adicionales = models.TextField(max_length=150)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    completado = models.BooleanField()
    def __str__(self):
        return self.ejercicio.nombre_ejercicio+'-'+self.programa.paciente.nombre+'-'+str(self.semana)+'-'+self.fecha_ejercicio.strftime('%A') 


class Resultado(models.Model):
    comentarios = models.TextField(max_length=300)
    completado = models.BooleanField()
    evidencia = models.FileField(upload_to='video', null=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_ejercicio = models.ForeignKey(Asignar_ejercicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_paciente.nombre+'-'+str(self.id_ejercicio.semana)+'-'+self.id_ejercicio.fecha_ejercicio.strftime('%A')

class Ejercicio_Pomo(models.Model):
    nombre_ejercicio= models.CharField(max_length=30)
    detalle_ejercicio = models.TextField(max_length=150)
    video = models.FileField(upload_to='video', null=True)
    def __str__(self):
        return self.nombre_ejercicio
