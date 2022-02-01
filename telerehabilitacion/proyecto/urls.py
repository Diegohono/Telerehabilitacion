from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [ 
    url(r'^$', views.index, name="Inicio"), 
    url(r'^paciente/$', views.paciente, name="Paciente"), 
    url(r'^crear_ejercicio/$', views.crear_ejercicios, name="Crear_Ejercicio"), 
    url(r'^kine/$', views.kine, name="kine"), 
    url(r'^Crear_paciente/$', views.crear_paciente, name="crear_paciente"),
    url(r'^paciente/(?P<id>[0-9]+)/$', views.detalle_semana, name="detalle_semana"), 
    url(r'^kine/(?P<pk>[0-9]+)/$', views.detalle_paciente, name="detalle_paciente"), 
    url(r'^kine/paciente/eliminar/(?P<id>[0-9]+)/$', views.eliminar_paciente, name="eliminar_paciente"),
    url(r'^paciente/preparación/(?P<pk>[0-9]+)/$',views.ejercicios, name='ejercicios'),
    url(r'^paciente/preparación/ejercicio/(?P<pk>[0-9]+)/$',views.rutina, name='rutina'),
    url(r'^lista/ejercicios/$', views.listar_ejercicios, name="listar_ejercicios"), 
    url(r'^lista/ejercicios/modificar/(?P<id>[0-9]+)/$', views.modificar_ejercicio, name="modificar_ejercicio"), 
    url(r'^lista/ejercicios/eliminar/(?P<id>[0-9]+)/$', views.eliminar_ejercicio, name="eliminar_ejercicio"),
    url(r'^kine/semana/(?P<id>[0-9]+)/paciente/(?P<pa>[0-9]+)/$', views.detalle_paciente_semanal, name="detalle_paciente_semanal"), 
    url(r'^kine/paciente/(?P<id>[0-9]+)/rutina/$', views.crear_rutina, name="crear_rutina"), 
    url(r'^kine/ejercicio/semana/(?P<semana>[0-9]+)/paciente/(?P<id>[0-9]+)/$', views.añadir_ejercicio, name="añadir_ejercicio"), 
    url(r'^kine/paciente/(?P<pa>[0-9]+)/rutina/editar/(?P<id>[0-9]+)/$', views.editar_rutina, name="editar_rutina"), 
    url(r'^kine/paciente/(?P<pa>[0-9]+)/ejercicio/(?P<id>[0-9]+)/resultado/$', views.mostrar_resultado, name="mostrar_resultado"), 
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)