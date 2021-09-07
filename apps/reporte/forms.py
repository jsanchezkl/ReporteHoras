from django import forms
from django.forms import fields, models, widgets
from apps.reporte.models import Reporte

class ReporteForm (forms.ModelForm):

    class Meta:
        model = Reporte
        fields = [
            'fecha',
            'descripcion',
            'horas',
            'campania',
            'actividad',
        ] 
        labels = {
            'fecha': 'Fecha',
            'descripcion': 'Descipción de actividad',
            'horas': 'Horas',
            'campania':'Nombre campaña',
            'actividad': 'Actividad',
        }
        widgets ={
            'fecha': forms.DateInput(attrs={'type': 'date' ,'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'horas': forms.TextInput(attrs={'class':'form-control'}),
            'campania': forms.Select(attrs={'class':'form-control'}),
            'actividad': forms.Select(attrs={'class':'form-control'}),
        } 
            
        