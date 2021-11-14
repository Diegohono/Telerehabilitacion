from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'telerehabilitacion/Index.html',{})

def crear_ejercicios(request):
    return render(request, 'telerehabilitacion/CrearEjercicios.html',{})

def kine(request):
    return render(request, 'telerehabilitacion/kine.html',{})

def paciente(request):
    return render(request, 'telerehabilitacion/Paciente.html',{})