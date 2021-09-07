from django import forms
from django.forms import fields, models, widgets
from apps.campania.models import Campania

class CampaniaForm (forms.ModelForm):

    class Meta:
        model = Campania
        fields = [
            'codigo',
            'linea',
            'nombre',
        ] 
        labels = {
            'codigo': 'Codigo',
            'linea': 'Linea de negocio',
            'nombre': 'Nombre de la campaña',
        }
        widgets ={
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'linea': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        } 
            
        