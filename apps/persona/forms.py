from django import forms
from django.forms import fields, models, widgets
from apps.persona.models import Persona

class PersonaForm (forms.ModelForm):

    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'masivo',
            'cargo',
            'horas_total',
            'porc_establecido',
        ] 
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'masivo': 'Masivo',
            'cargo': 'Cargo',
            'horas_total': 'Horas total',
            'porc_establecido': 'Porcentaje establecido',
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'masivo': forms.TextInput(attrs={'class':'form-control'}),
            'cargo': forms.TextInput(attrs={'class':'form-control'}),
            'horas_total': forms.TextInput(attrs={'class':'form-control'}),
            'porc_establecido': forms.TextInput(attrs={'class':'form-control'}),
        } 
            
        