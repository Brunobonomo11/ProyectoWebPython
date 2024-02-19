from django.contrib import admin
from django.urls import path
from AppAutos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio),
    
    path("autos/", ver_autos, name="Autos"),
    path("camionetas/", ver_camionetas, name="Camionetas"),
    path("camiones/", ver_camiones, name="Camiones"),
    
    path("nuevoAuto/", agregar_auto),
    path("nuevaCamioneta/", agregar_camioneta),
    path("nuevoCamion/", agregar_camion),
]
