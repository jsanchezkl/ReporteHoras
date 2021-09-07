from typing import List
from django.db import models
from django.urls.base import reverse_lazy
from django.urls import reverse_lazy

from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView,CreateView, UpdateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from apps.persona.forms import PersonaForm
from apps.persona.models import Persona
# Create your views here.

def index(request):
    return render(request, 'persona/index.html')

class PersonaList (ListView):
    model = Persona
    template_name = 'persona/persona_list.html'

class PersonaCreate (CreateView):
    models = Persona
    form_class = PersonaForm
    template_name = 'persona/persona_form.html'
    success_url = reverse_lazy ('persona_listar')