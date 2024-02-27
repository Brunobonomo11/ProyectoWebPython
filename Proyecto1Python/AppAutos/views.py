from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from AppAutos.models import Autos, Camionetas, Camiones
from AppAutos.forms import AutosFormulario, CamionetasFormulario, CamionesFormulario

def inicio(request):
    
    return render(request, "AppAutos/inicio.html")

#Vistas de register/login/logout

def inicio_sesion(request):
    
    if request.method == "POST":
        
        formulario = AuthenticationForm(request, data = request.POST)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            
            usuario = info["username"]
            contraseña = info["password"]
            
            usuario_actual = authenticate(username=usuario, password=contraseña)
            
            
            if usuario_actual is not None:
                login(request, usuario_actual)
                
                return render(request, "AppAutos/inicio.html", {"mensaje":f"Bienvenido {usuario}!"})
            else: 
                
                return render(request, "AppAutos/inicio.html", {"mensaje":"Error, los datos ingresados son incorrectos"})
            
        else:
            
            return render(request, "AppAutos/inicio.html", {"mensaje":"Error, el formulario es incorrecto"})
        
    formulario = AuthenticationForm()
    
    
    return render(request, "registro/inicio_sesion.html", {"formu": formulario})

def registro(request):
    
    if request.method == "POST":
        
        formulario = UserCreationForm(request.POST)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            
            usuario = info["username"]
            
            formulario.save() # Se crea el usuario en la base de datos
            
            return render(request, "AppAutos/inicio.html", {"mensaje":f"Bienvenido {usuario} !"})
    
    formulario = UserCreationForm()
    
    return render(request, "registro/registrar_usuario.html", {"formu":formulario})



# Create your views here.

#CRUD de Autos

# C (Create) del CRUD
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
    
    
#CRUD de Camionetas

# C (Create) del CRUD
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
            
            nuevo_formulario = AutosFormulario()
    
        return render(request, "AppAutos/formu_camioneta.html", {"mi_formu":nuevo_formulario})
    

#CRUD de Camiones

# C (Create) del CRUD
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
            
            nuevo_formulario = AutosFormulario()
    
        return render(request, "AppAutos/formu_camion.html", {"mi_formu":nuevo_formulario})
    

#R (read) del CRUD
def ver_autos(request):
    
    mis_autos = Autos.objects.all() #Obtenemos todo el listado de autos en mi tabla Autos
    
    info = {"autos":mis_autos}
    
    return render(request, "AppAutos/autos.html", info)


#R (read) del CRUD de camionetas
def ver_camionetas(request):
    
    mis_camionetas = Camionetas.objects.all() #Obtenemos todo el listado de autos en mi tabla Autos
    
    info = {"camionetas":mis_camionetas}
    
    return render(request, "AppAutos/camionetas.html", info)



#R (read) del CRUD de camiones
def ver_camiones(request):
    
    mis_camiones = Camiones.objects.all() #Obtenemos todo el listado de autos en mi tabla Autos
    
    info = {"camiones":mis_camiones}
    
    return render(request, "AppAutos/camiones.html", info)


#U (update) del CRUD de Autos

def actualizar_auto(request, autos_marca):
    
    # ¿Qué auto quiero actualizar?
    camion_escogido = Autos.objects.get(marca=autos_marca) #Encuentro el auto que quiero actualizar
        
    #Obtener los datos del formulario HTML
    nuevo_formulario = AutosFormulario(request.POST)
        
    #Depende de darle click al botón enviar o guardar
    if request.method == "POST":
        
        if nuevo_formulario.is_valid():
            
                #Para tenerlos en modo diccionario
                info = nuevo_formulario.cleaned_data 
                
                #Actualizar info del auto escogido
                camion_escogido.marca = info["marca"]
                camion_escogido.modelo = info["modelo"]
                camion_escogido.año = info["año"]
                camion_escogido.color = info["color"]
                
                camion_escogido.save()
                
                return render(request, "AppAutos/inicio.html")
            
        else: #Si la persona no ha hecho click al botón enviar
            
            nuevo_formulario = AutosFormulario()
    
    return render(request, "AppAutos/update_auto.html", {"mi_formu":nuevo_formulario})


#D (Delete) del CRUD de Autos

def eliminar_auto(request, autos_marca):
    
    camion_escogido = Autos.objects.get(marca=autos_marca)
    
    camion_escogido.delete()
    
    return render(request, "AppAutos/autos.html")



#U (update) del CRUD de Camionetas

def actualizar_camioneta(request, camionetas_marca):
    
    # ¿Qué auto quiero actualizar?
    camion_escogido = Camionetas.objects.get(marca=camionetas_marca) #Encuentro el auto que quiero actualizar
        
    #Obtener los datos del formulario HTML
    nuevo_formulario = CamionetasFormulario(request.POST)
        
    #Depende de darle click al botón enviar o guardar
    if request.method == "POST":
        
        if nuevo_formulario.is_valid():
            
                #Para tenerlos en modo diccionario
                info = nuevo_formulario.cleaned_data 
                
                #Actualizar info del auto escogido
                camion_escogido.marca = info["marca"]
                camion_escogido.modelo = info["modelo"]
                camion_escogido.año = info["año"]
                camion_escogido.color = info["color"]
                
                camion_escogido.save()
                
                return render(request, "AppAutos/inicio.html")
            
        else: #Si la persona no ha hecho click al botón enviar
            
            nuevo_formulario = CamionetasFormulario()
    
    return render(request, "AppAutos/update_camionetas.html", {"mi_formu":nuevo_formulario})


#D (Delete) del CRUD de Camionetas

def eliminar_camioneta(request, camionetas_marca):
    
    camion_escogido = Camionetas.objects.get(marca=camionetas_marca)
    
    camion_escogido.delete()
    
    return render(request, "AppAutos/camionetas.html")


#U (update) del CRUD de Camiones

def actualizar_camion(request, camiones_marca):
    
    # ¿Qué auto quiero actualizar?
    camion_escogido = Camiones.objects.get(marca=camiones_marca) #Encuentro el auto que quiero actualizar
        
    #Obtener los datos del formulario HTML
    nuevo_formulario = CamionesFormulario(request.POST)
        
    #Depende de darle click al botón enviar o guardar
    if request.method == "POST":
        
        if nuevo_formulario.is_valid():
            
                #Para tenerlos en modo diccionario
                info = nuevo_formulario.cleaned_data 
                
                #Actualizar info del auto escogido
                camion_escogido.marca = info["marca"]
                camion_escogido.modelo = info["modelo"]
                camion_escogido.año = info["año"]
                camion_escogido.color = info["color"]
                
                camion_escogido.save()
                
                return render(request, "AppAutos/inicio.html")
            
        else: #Si la persona no ha hecho click al botón enviar
            
            nuevo_formulario = CamionesFormulario()
    
    return render(request, "AppAutos/update_camiones.html", {"mi_formu":nuevo_formulario})


#D (Delete) del CRUD de Camionetas

def eliminar_camion(request, camiones_marca):
    
    camion_escogido = Camiones.objects.get(marca=camiones_marca)
    
    camion_escogido.delete()
    
    return render(request, "AppAutos/camiones.html")




#CRUD de Camionetas


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
        

# CRUD de Autos (Vistas basadas en clases)

#R (Read) de Autos --- ListView

class ListaAutos(ListView):
    
    model = Autos
    template_name = "AppAutos/Autos_List.html"
    
class CrearAutos(CreateView):
    
    model = Autos
    template_name = "AppAutos/crearAutos.html"
    fields = ["marca", "modelo", "año", "color"]
    success_url = "/listaAutos"
    
class ActualizarAutos(UpdateView):
    
    model = Autos
    template_name = "AppAutos/crearAutos.html"
    fields = ["marca", "modelo", "año", "color"]
    success_url = "/listaAutos"
    
class BorrarAutos(DeleteView):
    
    model = Autos
    template_name = "AppAutos/borrarAuto.html"
    success_url = "/listaAutos/"
    
    
    
    

class ListaCamionetas(ListView):
    
    model = Camionetas
    template_name = "AppAutos/Camionetas_List.html"
    
class CrearCamionetas(CreateView):
    
    model = Camionetas
    template_name = "AppAutos/crearCamionetas.html"
    fields = ["marca", "modelo", "año", "color"]
    success_url = "/listaCamionetas"
    
class ActualizarCamionetas(UpdateView):
    
    model = Camionetas
    template_name = "AppAutos/crearCamionetas.html"
    fields = ["marca", "modelo", "año", "color"]
    success_url = "/listaCamionetas"
    
class BorrarCamionetas(DeleteView):
    
    model = Camionetas
    template_name = "AppAutos/borrarCamioneta.html"
    success_url = "/listaCamionetas/"
    
    
    
    
class ListaCamiones(ListView):
    
    model = Camiones
    template_name = "AppAutos/Camiones_List.html"
    
class CrearCamiones(CreateView):
    
    model = Camiones
    template_name = "AppAutos/crearCamiones.html"
    fields = ["marca", "modelo", "año", "color"]
    success_url = "/listaCamiones"
    
class ActualizarCamiones(UpdateView):
    
    model = Camiones
    template_name = "AppAutos/crearCamiones.html"
    fields = ["marca", "modelo", "año", "color"]
    success_url = "/listaCamiones"
    
class BorrarCamiones(DeleteView):
    
    model = Camiones
    template_name = "AppAutos/borrarCamion.html"
    success_url = "/listaCamiones/"


