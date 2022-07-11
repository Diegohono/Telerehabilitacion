from django import forms
from .models import Ejercicio

class Ejercicio1(forms.ModelForm):
    class Meta:
        model=Ejercicio
        fields=("nombre_ejercicio","detalle_ejercicio","video","id_kinesiologo")