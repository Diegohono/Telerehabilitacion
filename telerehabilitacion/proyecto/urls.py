from django.urls import include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [ 
    re_path(r'^$', views.index, name="Inicio"), 
    re_path(r'^paciente/$', views.paciente, name="Paciente"), 
    re_path(r'^test/$', views.Test, name="test"), 
    re_path(r'^crear_ejercicio/$', views.crear_ejercicios, name="Crear_Ejercicio"), 
    re_path(r'^kine/$', views.kine, name="kine"), 
    re_path(r'^Crear_paciente/$', views.crear_paciente, name="crear_paciente"),
    re_path(r'^paciente/(?P<id>[0-9]+)/$', views.detalle_semana, name="detalle_semana"), 
    re_path(r'^kine/(?P<pk>[0-9]+)/$', views.detalle_paciente, name="detalle_paciente"), 
    re_path(r'^kine/paciente/eliminar/(?P<id>[0-9]+)/$', views.eliminar_paciente, name="eliminar_paciente"),
    re_path(r'^paciente/preparación/(?P<pk>[0-9]+)/$',views.ejercicios, name='ejercicios'),
    re_path(r'^paciente/preparación/ejercicio/(?P<pk>[0-9]+)/$',views.rutina, name='rutina'),
    re_path(r'^lista/ejercicios/$', views.listar_ejercicios, name="listar_ejercicios"), 
    re_path(r'^lista/ejercicios/modificar/(?P<id>[0-9]+)/$', views.modificar_ejercicio, name="modificar_ejercicio"), 
    re_path(r'^lista/ejercicios/eliminar/(?P<id>[0-9]+)/$', views.eliminar_ejercicio, name="eliminar_ejercicio"),
    re_path(r'^kine/semana/(?P<id>[0-9]+)/paciente/(?P<pa>[0-9]+)/$', views.detalle_paciente_semanal, name="detalle_paciente_semanal"), 
    re_path(r'^kine/paciente/(?P<id>[0-9]+)/rutina/$', views.crear_rutina, name="crear_rutina"), 
    re_path(r'^kine/ejercicio/semana/(?P<semana>[0-9]+)/paciente/(?P<id>[0-9]+)/$', views.añadir_ejercicio, name="añadir_ejercicio"), 
    re_path(r'^kine/paciente/(?P<pa>[0-9]+)/rutina/editar/(?P<id>[0-9]+)/$', views.editar_rutina, name="editar_rutina"), 
    re_path(r'^kine/paciente/(?P<pa>[0-9]+)/ejercicio/(?P<id>[0-9]+)/resultado/$', views.mostrar_resultado, name="mostrar_resultado"), 
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
