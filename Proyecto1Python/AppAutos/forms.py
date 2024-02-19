from django import forms

class AutosFormulario(forms.Form):
    
    marca=forms.CharField()
    modelo=forms.CharField()
    año=forms.IntegerField()
    color=forms.CharField()
    
class CamionetasFormulario(forms.Form):
    
    marca=forms.CharField()
    modelo=forms.CharField()
    año=forms.IntegerField()
    color=forms.CharField()
    
class CamionesFormulario(forms.Form):
    
    marca=forms.CharField()
    modelo=forms.CharField()
    año=forms.IntegerField()
    color=forms.CharField()
    