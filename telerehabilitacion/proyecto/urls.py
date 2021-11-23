from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [ 
    url(r'^$', views.index, name="Inicio"), 
    url(r'^paciente/$', views.paciente, name="Paciente"), 
    url(r'^crear_ejercicio/$', views.crear_ejercicios, name="Crear_Ejercicio"), 
    url(r'^kine/$', views.kine, name="kine"), 
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)