from typing import List
from django.db import models
from django.urls.base import reverse_lazy
from django.urls import reverse_lazy

from django.views.generic import ListView,CreateView, UpdateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from apps.actividad.forms import ActividadForm
from apps.actividad.models import Actividad
# Create your views here.

def index(request):
    return render(request, 'actividad/index.html')

class ActividadList (ListView):
    model = Actividad
    template_name = 'actividad/actividad_list.html'

class ActividadCreate (CreateView):
    models = Actividad
    form_class = ActividadForm
    template_name = 'actividad/actividad_form.html'
    success_url = reverse_lazy ('actividad_listar')

class ActividadUpdate (UpdateView):
    models = Actividad
    form_class = ActividadForm
    template_name = 'actividad/actividad_form.html'
    success_url = reverse_lazy ('actividad_listar')

class ActividadDelete (DeleteView):
    model = Actividad
    template_name = 'actividad/actividad_delete.html'
    success_url = reverse_lazy ('actividad_listar')
