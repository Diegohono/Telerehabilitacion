from io import UnsupportedOperation
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from .models import Ciudad, Kinesiologo, Paciente, Usuario
# Create your views here.

def index(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('password')
        userLogin = authenticate(request,username=usuario, password=contraseña)
        try:
            if userLogin is not None:
                login(request, userLogin)
                userA = request.user
                try:
                    if Kinesiologo.objects.get(userD=userA):
                        return redirect(to="kine")
                   
                except:
                    if Paciente.objects.get(userD=userA):
                        return redirect(to="Paciente")

        except:
           pass
                
    return render(request, 'telerehabilitacion/Index.html',{})

def crear_ejercicios(request):
    return render(request, 'telerehabilitacion/CrearEjercicios.html',{})

def kine(request):
    pac= Paciente.objects.all()
    ciudad = Ciudad.objects.all()
    data={
        'pac':pac,
        'ciudad':ciudad,
    }
    return render(request, 'telerehabilitacion/kine.html',data)

def paciente(request):
    return render(request, 'telerehabilitacion/Paciente.html',{})

def crear_paciente(request):
    pa = Paciente()
    U = User()
    U.username = request.POST.get('nombre')
    U.set_password(request.POST.get('contraseña'))
    txt= ''
    data={
        'txt':txt,
    }
    try:
        U.save()
        pa.userD= U
        pa.nombre = request.POST.get('nombre')
        pa.a_paterno = request.POST.get('paterno')
        pa.a_materno = request.POST.get('materno')
        pa.fecha_nacimiento = request.POST.get('fecha')
        pa.telefono = request.POST.get('numero')
        ci = Ciudad()
        ci.ciudad = request.POST.get('ciudad')
        ci.save()
        pa.id_ciudad = ci
        pa.save()
        if Paciente.objects.filter(userD = pa.userD).exists():
            txt = 'usuario creado con éxito'
        else:
            txt = 'usuario no creado'
            U.delete()
    except:
        pass        
    data={
        'txt':txt,
    }
    return render(request, 'telerehabilitacion/CrearPaciente.html',data)

def detalle_paciente(request, pk):
    pa = get_object_or_404(Paciente, pk = pk)
    return render(request, 'telerehabilitacion/detalle_paciente.html')