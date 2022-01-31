from django.contrib import admin
from .models import Asignar_ejercicio, Ejercicio_Pomo,Kinesiologo,Familiar,Paciente,Ejercicio, Programa,Resultado
# Register your models here.


admin.site.register(Kinesiologo)
admin.site.register(Familiar)
admin.site.register(Paciente)
admin.site.register(Ejercicio)
admin.site.register(Resultado)
admin.site.register(Asignar_ejercicio)
admin.site.register(Programa)
admin.site.register(Ejercicio_Pomo)
