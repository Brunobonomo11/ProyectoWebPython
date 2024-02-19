from django.shortcuts import render
from django.http import HttpResponse
from AppAutos.models import Autos, Camionetas, Camiones


def ver_autos(request):
    
    mis_autos = Autos.objects.all() #Obtenemos todo el listado de autos en mi tabla Autos
    
    info = {"autos":mis_autos}
    
    return render(request, "AppAutos/autos.html", info)

def inicio(request):
    
    return render(request, "AppAutos/inicio.html")


def ver_camionetas(request):
    
    return render(request, "AppAutos/camionetas.html")

def ver_camiones(request):
    
    return render(request, "AppAutos/camiones.html")



# Create your views here.

def agregar_auto(request):
    
    auto1 = Autos(marca="Renault", modelo="Clio Mio", año=2012, color="Gris")
    auto1.save()
    
    return HttpResponse("Se agregó un auto nuevo...")


def agregar_camioneta(request):
    
    camioneta1 = Camionetas(marca="Ford", modelo="Raptor F-150", año=2022, color="Azul")
    camioneta1.save()
    
    return HttpResponse("Se agregó una camioneta nueva...")


def agregar_camion(request):
    
    camion1 = Camiones(marca="Mercedes Benz", modelo="Atego 1725/42", año=2014, color="Blanco")
    camion1.save()
    
    return HttpResponse("Se agregó un camion nuevo...")



