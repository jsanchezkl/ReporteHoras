from proy_horas.settings import TEMPLATES
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

from apps.usuarios.forms import RegistroForm
# Create your views here.

class RegistroUsuario (CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy ('reporte_listar')

