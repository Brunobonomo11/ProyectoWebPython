from django.db import models

# Create your models here.

class Autos(models.Model):
    
            marca = models.CharField(max_length=40)
            modelo = models.CharField(max_length=40)
            año =  models.IntegerField()
            color = models.CharField(max_length=40)
    
class Camionetas(models.Model):
    
            marca = models.CharField(max_length=40)
            modelo = models.CharField(max_length=40)
            año =  models.IntegerField()
            color = models.CharField(max_length=40)
            
class Camiones(models.Model):
    
            marca = models.CharField(max_length=40)
            modelo = models.CharField(max_length=40)
            año =  models.IntegerField()
            color = models.CharField(max_length=40)