from django.contrib import admin
from django.urls import path
from AppAutos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", inicio),
    
    # URLs de los modelos creados
    path("autos/", ver_autos, name="Autos"),
    path("camionetas/", ver_camionetas, name="Camionetas"),
    path("camiones/", ver_camiones, name="Camiones"),
    
    #Urls para crear nuevos datos
    path("nuevoAuto/", agregar_auto),
    path("nuevaCamioneta/", agregar_camioneta),
    path("nuevoCamion/", agregar_camion),
    
    #URLs para buscar datos
    path("buscarAutoAño/", busqueda_auto_año),
    path("resultadosAutos/", resultados_buscar_auto_año),
]
