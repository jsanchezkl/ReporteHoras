from django import forms
from django.forms import fields, models, widgets
from apps.actividad.models import Actividad

class ActividadForm (forms.ModelForm):

    class Meta:
        model = Actividad
        fields = [
            'nombre',
        ] 
        labels = {
            'nombre': 'Nombre',
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        } 
            
        