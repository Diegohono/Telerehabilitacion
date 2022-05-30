from ast import Try
from distutils.command.upload import upload
from http.client import REQUEST_ENTITY_TOO_LARGE
from io import UnsupportedOperation
#from turtle import up
from webbrowser import get
from xmlrpc.client import DateTime
#from django import views
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from .models import Ejercicio, Kinesiologo, Paciente, Programa, Resultado, Usuario, Asignar_ejercicio
from django.db.models import Q
import datetime
# Create your views here.

#pagina de inicio de sesion
def index(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('password')
        userLogin = authenticate(request,username=usuario, password=contraseña)
        #valida que tipo de usuario se está iniciando sesión
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

#vista donde el kinesiologo crea los ejercicios
def crear_ejercicios(request):
    try:
        if request.method == 'POST':
            eje = Ejercicio()
            eje.nombre_ejercicio = request.POST.get('nombre') 
            eje.video = request.POST.get('Video') 
            eje.detalle_ejercicio = request.POST.get('Detalle-ejercicio')
            U = request.user
            K = Kinesiologo.objects.get(userD = U)
            eje.id_kinesiologo = K
            eje.save()
    except:
        pass
    return render(request, 'telerehabilitacion/CrearEjercicios.html',{})

#vista kinesilogo
def kine(request):
    UK = request.user
    K = Kinesiologo.objects.get(userD = UK)
    pac= Paciente.objects.filter(id_kinesiologo = K)
    data={
        'pac':pac,
    }
    
    return render(request, 'telerehabilitacion/kine.html',data)

def listar_ejercicios(request):
    U = request.user
    K = Kinesiologo.objects.get(userD = U)
    ejercicio = Ejercicio.objects.filter(id_kinesiologo=K)
    data={
        'ejercicio':ejercicio
    }
    return render(request, 'telerehabilitacion/lista-ejercicio.html', data)

#vista paciente
def paciente(request):
    U = User()
    U = request.user
    P = Paciente.objects.get(userD=U)
    programa = get_object_or_404(Programa,paciente=P)
    ejercicio = Asignar_ejercicio.objects.all()
    semanas = Programa.objects.only('cantidad_semanas').get(paciente=P).cantidad_semanas
    #arreglo donde se cuentan las semanas 
    lista = []
    for i in range(semanas):
        lista.append(i+1)

    data = {
        'paciente':P,
        'programa':programa,
        'lista':lista,
        'ejercicio':ejercicio,

    }
    return render(request, 'telerehabilitacion/Paciente.html',data)

def crear_paciente(request):
    txt=''
    if request.method == 'POST':
        pa = Paciente()
        U = User()
        U.username = request.POST.get('rut')
        U.set_password(request.POST.get('contraseña'))
        txt= ''
        try:
            pa.userD= U
            pa.nombre = request.POST.get('nombre')
            pa.a_paterno = request.POST.get('paterno')
            pa.a_materno = request.POST.get('materno')
            pa.fecha_nacimiento = request.POST.get('fecha')
            pa.telefono = request.POST.get('numero')
            pa.ciudad = request.POST.get('ciudad')
            pa.rut = request.POST.get('rut')
            
            pa.foto = request.POST.get('foto')
            UK = request.user
            K = Kinesiologo.objects.get(userD = UK)
            pa.id_kinesiologo = K
            U.save()
            pa.save()
            if Paciente.objects.filter(userD = pa.userD).exists():
                txt = 'usuario creado con éxito'
            else:
                txt = 'usuario no creado'
                U.delete()
        except:
            txt = 'usuario no creado'        
    data={
        'txt':txt,
    }
    return render(request, 'telerehabilitacion/CrearPaciente.html',data)

#vista del detalle del paciente, con parametro pk = id del paciente
def detalle_paciente(request, pk):
    pa = get_object_or_404(Paciente, pk = pk)
    if Programa.objects.filter(paciente=pa).exists():
        programa = get_object_or_404(Programa,paciente=pa)
        ejercicio = Asignar_ejercicio.objects.all()
        semanas = Programa.objects.only('cantidad_semanas').get(paciente=pa).cantidad_semanas
        lista = []
        for i in range(semanas):
            lista.append(i+1)
    else:
        return redirect(to="crear_rutina",id=pk)
    
    data={
        'pa':pa,
        'programa':programa,
        'lista':lista,
        'ejercicio':ejercicio,
        'pk':pk,

    }
    return render(request, 'telerehabilitacion/detalle_paciente.html', data)

#parametros id = id del ejercicio
def eliminar_paciente(request,id):
    paciente = get_object_or_404(Paciente, id=id)
    usuario = User.objects.get(username=paciente.userD)
    usuario.delete()
    paciente.delete()
    return redirect(to='kine')


#detalle de la semana del paciente, parametro id = numero de la semana, pa = paciente como objeto tipo Paciente()
def detalle_paciente_semanal(request, id, pa):
    semana = id
    ejercicio = Asignar_ejercicio.objects.filter(Q(semana=id))
    programa = get_object_or_404(Programa,paciente=pa)
    resultado = Resultado.objects.all()

    data={
        'semana':semana,
        'ejercicio':ejercicio,
        'resultado':resultado,
        'pa':pa,
        'programa':programa,
    }
    return render(request, 'telerehabilitacion/detalle_paciente_semanal.html', data)

#Se crea la rutina, parametro id = id del paciente
def crear_rutina(request,id):
    pa = get_object_or_404(Paciente, pk = id)
    if request.method == 'POST':
        #si el programa existe, se borra y se crea hace nuevamente
        if Programa.objects.filter(paciente=pa).exists():
            Programa.objects.filter(paciente=pa).delete()
            programa = Programa()
            pa = Paciente()
            pa.pk = id
            programa.paciente = pa
            programa.cantidad_semanas = request.POST.get('cantidad_semanas')
            programa.save()
            return redirect('detalle_paciente',pk=id)
        else:
            programa = Programa()
            pa = Paciente()
            pa.pk = id
            programa.paciente = pa
            programa.cantidad_semanas = request.POST.get('cantidad_semanas')
            programa.save()
            return redirect('detalle_paciente',pk=id)
    return render(request, 'telerehabilitacion/Crear_rutina.html')

#vista para asignar ejercicio al paciente
#parametros id = id del paciente, semana = semana en la que se creara la rutina
def añadir_ejercicio(request,id,semana):
    pa = get_object_or_404(Paciente, pk = id)
    U = request.user
    K = Kinesiologo.objects.get(userD = U)
    UP = User.objects.get(username='pomo')
    P = Kinesiologo.objects.get(userD = UP)
    #se filtra por kinesiologo logeado y por usuario "pomo"
    ejercicio = Ejercicio.objects.filter(Q(id_kinesiologo=P)|Q(id_kinesiologo=K))
    if request.method == 'POST':
        if 'añadir_ejercicio' in request.POST:
            asignar = Asignar_ejercicio()
            ejer = get_object_or_404(Ejercicio,id=request.POST.get('seleccionar_ejercicio'))
            asignar.ejercicio = ejer
            asignar.fecha_ejercicio = datetime.datetime.today()
            asignar.semana = semana
            eje = Asignar_ejercicio.objects.all()
            programa = Programa.objects.filter(paciente=pa)
            #se calcula el programa y el numero de ejercicio que corresponde
            for i in programa:
                asignar.programa=i
                pass
            cantidad = 0
            for i in eje:
                if i.programa == programa and i.semana == semana:
                    cantidad = cantidad + 1
            asignar.n_ejercicio=cantidad+1
            asignar.comentarios_adicionales=request.POST.get('comentarios')
            asignar.completado=False
            asignar.save()
            return redirect(to='detalle_paciente',pk=id)
   
    data={
        'ejercicio':ejercicio,
        'semana':semana,
        'pa':pa,
    }
    return render(request, 'telerehabilitacion/añadir_ejercicio.html',data)

#parametros id = id del ejercicio
def modificar_ejercicio(request,id):
    ejercicio = get_object_or_404(Ejercicio, id=id)
    try:
        if request.method == 'POST':
            
            ejercicio.nombre_ejercicio = request.POST.get('nombre') 
            ejercicio.video = request.POST.get('Video') 
            ejercicio.detalle_ejercicio = request.POST.get('Detalle-ejercicio')
            U = request.user
            K = Kinesiologo.objects.get(userD = U)
            ejercicio.id_kinesiologo = K
            ejercicio.save()
            return redirect(to='listar_ejercicios')
    except:
        pass
    data={
        'ejercicio':ejercicio,
    }
    return render(request, 'telerehabilitacion/modificar_ejercicio.html', data)

#parametros id = id del ejercicio
def eliminar_ejercicio(request,id):
    ejercicio = get_object_or_404(Ejercicio, id=id)
    ejercicio.delete()
    return redirect(to='listar_ejercicios')

#parametros id = id de la rutina(Asignar_ejercicio), pa = id del paciente para direccionar una vez editada
def editar_rutina(request,id,pa):
    U = request.user
    K = Kinesiologo.objects.get(userD = U)
    UP = User.objects.get(username='pomo')
    P = Kinesiologo.objects.get(userD = UP)
    ejercicio = Ejercicio.objects.filter(Q(id_kinesiologo=P)|Q(id_kinesiologo=K))
    ed_rutina = get_object_or_404(Asignar_ejercicio, id=id)
    if request.method == 'POST':
        if 'añadir_ejercicio' in request.POST:
            asignar = get_object_or_404(Asignar_ejercicio, id=id)
            if request.POST.get('seleccionar_ejercicio'):
                ejer = get_object_or_404(Ejercicio,id=request.POST.get('seleccionar_ejercicio'))
                asignar.ejercicio = ejer
            asignar.comentarios_adicionales=request.POST.get('comentarios')
            asignar.save()
            return redirect(to='detalle_paciente',pk=pa)
    data={
        'ejercicio':ejercicio,
        'rutina':ed_rutina,
    }
    return render(request, 'telerehabilitacion/editar_rutina.html', data)

#parametro pa = id del paciente, id= id de rutina(Asignar_ejercicio)
def mostrar_resultado(request,pa,id):
    #resultado = get_object_or_404(Resultado,id_paciente=pa)
    ejercicio = Asignar_ejercicio.objects.get(id=id)
    resultado = Resultado.objects.filter(Q(id_paciente=pa),Q(id_ejercicio=ejercicio))
    data={
        'resultado':resultado
    }
    return render(request, 'telerehabilitacion/mostrar_resultado.html', data)

#parametro id = numero de semana 
def detalle_semana(request,id):
    semana = id
    ejercicio = Asignar_ejercicio.objects.filter(semana=id)
    resultado = Resultado.objects.all()

    data={
        'semana':semana,
        'ejercicio':ejercicio,
        'resultado':resultado,
    }
    return render(request,'telerehabilitacion/Detalle-Semana.html',data)

#parametro pk = id de la rutina(Asignar_ejercicio)
def ejercicios(request,pk):
    ejercicio = Asignar_ejercicio.objects.filter(pk=pk)
    data={
        'ejercicio':ejercicio,
    }
    return render(request,'telerehabilitacion/Ejercicios.html',data)

#parametro pk = id de la rutina(Asignar_ejercicio)
def rutina(request,pk):
    ejercicio = Asignar_ejercicio.objects.filter(pk=pk)
    if request.method == 'POST':
        resultado = Resultado()
        resultado.comentarios = request.POST.get('comentario')
        resultado.completado = True
        resultado.evidencia = request.POST.get('Foto/Video')
        usuario = request.user
        p = Paciente.objects.filter(userD = usuario)
        paciente = Paciente()
        for i in p:
            paciente.id= i.id
        print("el paciente es:" + str(paciente))
        resultado.id_paciente = paciente
        id_ejercicio = Asignar_ejercicio()
        id_ejercicio.pk=pk
        resultado.id_ejercicio = id_ejercicio
        id_ejercicio = Asignar_ejercicio.objects.get(pk=pk)
        id_ejercicio.completado = True
        id_ejercicio.save()
        resultado.save()
        return redirect(to="Paciente")
    data={
        'ejercicio':ejercicio,
    }
    return render(request,'telerehabilitacion/rutina.html',data)
