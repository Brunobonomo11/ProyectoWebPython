from django.contrib import admin
from django.urls import path
from AppAutos.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", inicio),
    
    path("login/", inicio_sesion, name="Iniciar Sesión"),
    path("signup/", registro, name="Registrarse"),
    path("logout/", cerrar_sesion, name="Cerrar Sesión"),
    
    # Creamos un auto y luego nos direcciona a la lista de Autos creados
    path("listaAutos/", ListaAutos.as_view(), name="Lista de Autos"),
    path("crearAutos/", CrearAutos.as_view(), name="Crear Autos"),
    path("actualizarAutos/<int:pk>", ActualizarAutos.as_view(), name="Actualizar Autos"),
    path("borrarAutos/<int:pk>", BorrarAutos.as_view(), name="Borrar Autos"),
    
    # Creamos una camioneta y luego nos direcciona a la lista de Camionetas creadas
    path("listaCamionetas/", ListaCamionetas.as_view(), name="Lista de Camionetas"),
    path("crearCamionetas/", CrearCamionetas.as_view(), name="Crear Camionetas"),
    path("actualizarCamionetas/<int:pk>", ActualizarCamionetas.as_view(), name="Actualizar Camionetas"),
    path("borrarCamionetas/<int:pk>", BorrarCamionetas.as_view(), name="Borrar Camionetas"),
    
    # Creamos un camion y luego nos direcciona a la lista de Camiones creados
    path("listaCamiones/", ListaCamiones.as_view(), name="Lista de Camiones"),
    path("crearCamiones/", CrearCamiones.as_view(), name="Crear Camiones"),
    path("actualizarCamiones/<int:pk>", ActualizarCamiones.as_view(), name="Actualizar Camiones"),
    path("borrarCamiones/<int:pk>", BorrarCamiones.as_view(), name="Borrar Camiones"),
    
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
