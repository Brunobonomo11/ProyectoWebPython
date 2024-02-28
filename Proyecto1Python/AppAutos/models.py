from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Autos(models.Model):
    
        def __str__(self):
            
            return f"{self.marca} {self.modelo} {self.año} {self.color}"
    
        marca = models.CharField(max_length=40)
        modelo = models.CharField(max_length=40)
        año =  models.IntegerField()
        color = models.CharField(max_length=40)
    
class Camionetas(models.Model):
    
        def __str__(self):
            
            return f"{self.marca} {self.modelo} {self.año} {self.color}"
    
        marca = models.CharField(max_length=40)
        modelo = models.CharField(max_length=40)
        año =  models.IntegerField()
        color = models.CharField(max_length=40)
            
class Camiones(models.Model):
    
        def __str__(self):
            
            return f"{self.marca} {self.modelo} {self.año} {self.color}"
    
        marca = models.CharField(max_length=40)
        modelo = models.CharField(max_length=40)
        año =  models.IntegerField()
        color = models.CharField(max_length=40)
        
class AvatarImagen(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    
    def __str__(self):
        
        return f"{self.usuario} --- {self.imagen}"