from django.contrib import admin
from .models import Ciudad,Kinesiologo,Familiar,Paciente,Ejercicio,Resultado
# Register your models here.

admin.site.register(Ciudad)
admin.site.register(Kinesiologo)
admin.site.register(Familiar)
admin.site.register(Paciente)
admin.site.register(Ejercicio)
admin.site.register(Resultado)