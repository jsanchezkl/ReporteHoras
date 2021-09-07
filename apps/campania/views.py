from typing import List
from django.db import models
from django.urls.base import reverse_lazy
from django.urls import reverse_lazy

from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView,CreateView, UpdateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from apps.campania.forms import CampaniaForm
from apps.campania.models import Campania
# Create your views here.

def index(request):
    return render(request, 'campania/index.html')

class CampaniaList (ListView):
    model = Campania
    template_name = 'campania/campania_list.html'

class CampaniaCreate (CreateView):
    models = Campania
    form_class = CampaniaForm
    template_name = 'campania/campania_form.html'
    success_url = reverse_lazy ('campania_listar')