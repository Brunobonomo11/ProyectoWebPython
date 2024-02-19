from django.contrib import admin
from django.urls import path
from AppAutos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", inicio),
    path("listaAutos/", ListaAutos.as_view(), name="Lista de Autos"),
    
    # URLs de los modelos creados
    path("autos/", ver_autos, name="Autos"),
    path("camionetas/", ver_camionetas, name="Camionetas"),
    path("camiones/", ver_camiones, name="Camiones"),
    
    #Urls para crear nuevos datos
    path("nuevoAuto/", agregar_auto, name="Nuevo Auto"),
    path("nuevaCamioneta/", agregar_camioneta, name="Nueva Camioneta"),
    path("nuevoCamion/", agregar_camion, name="Nuevo Camion"),
    
    #URLs para buscar datos
    path("buscarAutoAño/", busqueda_auto_año),
    path("resultadosAutos/", resultados_buscar_auto_año),
    
    #URLs para actualizar autos, camionetas, camion
    path("actualizarAuto/<autos_marca>", actualizar_auto, name="Actualizar Auto"),
    path("actualizarCamioneta/<camionetas_marca>", actualizar_camioneta, name="Actualizar Camioneta"),
    path("actualizarCamion/<camiones_marca>", actualizar_camion, name="Actualizar Camion"),
    
    #URLs para eliminar autos, camionetas, camion
    path("eliminarAuto/<autos_marca>", eliminar_auto, name="Eliminar Auto"),
    path("eliminarCamioneta/<camionetas_marca>", eliminar_camioneta, name="Eliminar Camioneta"),
    path("eliminarCamion/<camiones_marca>", eliminar_camion, name="Eliminar Camion"),
    
]
