from django.shortcuts import render
from django.http import HttpResponse
from AppAutos.models import Autos, Camionetas, Camiones
from AppAutos.forms import AutosFormulario, CamionetasFormulario, CamionesFormulario


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
    
    #Depende de darle click al botón enviar o guardar
        
        nuevo_formulario = AutosFormulario(request.POST)
        
        if request.method == "POST":
        
            if nuevo_formulario.is_valid():
                
                info = nuevo_formulario.cleaned_data
                
                auto_nuevo = Autos(marca=info["marca"], modelo=info["modelo"], año=info["año"], color=info["color"]) 
                
                auto_nuevo.save()
                
                return render(request, "AppAutos/inicio.html")
            
        else: #Si la persona no ha hecho click al botón enviar
            
            nuevo_formulario = AutosFormulario()
    
        return render(request, "AppAutos/formu_auto.html", {"mi_formu":nuevo_formulario})




def agregar_camioneta(request):
    
    #Depende de darle click al botón enviar o guardar
        
        nuevo_formulario = CamionetasFormulario(request.POST)
        
        if request.method == "POST":
        
            if nuevo_formulario.is_valid():
                
                info = nuevo_formulario.cleaned_data
                
                camioneta_nueva = Camionetas(marca=info["marca"], modelo=info["modelo"], año=info["año"], color=info["color"]) 
                
                camioneta_nueva.save()
                
                return render(request, "AppAutos/inicio.html")
            
        else: #Si la persona no ha hecho click al botón enviar
            
            nuevo_formulario = CamionetasFormulario()
    
        return render(request, "AppAutos/formu_camioneta.html", {"mi_formu":nuevo_formulario})




def agregar_camion(request):
    
    #Depende de darle click al botón enviar o guardar
        
        nuevo_formulario = CamionesFormulario(request.POST)
        
        if request.method == "POST":
        
            if nuevo_formulario.is_valid():
                
                info = nuevo_formulario.cleaned_data
                
                camion_nuevo = Camiones(marca=info["marca"], modelo=info["modelo"], año=info["año"], color=info["color"]) 
                
                camion_nuevo.save()
                
                return render(request, "AppAutos/inicio.html")
            
        else: #Si la persona no ha hecho click al botón enviar
            
            nuevo_formulario = CamionesFormulario()
    
        return render(request, "AppAutos/formu_camion.html", {"mi_formu":nuevo_formulario})
    

def busqueda_auto_año(request):
    
    return render(request, "AppAutos/buscar_auto_año.html")

  
def resultados_buscar_auto_año(request):
    
        if request.method=="GET":
            
            año_pedido = request.GET["año"]
            resultados_autos = Autos.objects.filter(año__icontains=año_pedido)
        
            return render(request, "AppAutos/buscar_auto_año.html", {"autos":resultados_autos}) 

    
        else:
            return render(request, "AppAutos/buscar_auto_año.html")



