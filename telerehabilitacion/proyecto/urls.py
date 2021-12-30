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
    url(r'^(?P<pk>[0-9]+)/$', views.detalle_paciente, name="detalle_paciente"), 
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)