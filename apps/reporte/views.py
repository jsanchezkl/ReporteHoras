from typing import List
from django.db import models
from django.urls.base import reverse_lazy
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView,CreateView, UpdateView
from django.forms.forms import Form

from django.contrib.auth.models import User

from apps.reporte.forms import ReporteForm
from apps.reporte.models import Reporte
# Create your views here.

def index(request):
    return render(request, 'reporte/index.html')

class ReporteList (ListView):
    model = Reporte
    template_name = 'reporte/reporte_list.html'
    def get_queryset(self, *args, **kwargs):
        return Reporte.objects.filter(usuario=self.request.user)
    paginate_by = 20

class ReporteCreate (LoginRequiredMixin, CreateView):
    models = Reporte
    form_class = ReporteForm    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    template_name = 'reporte/reporte_form.html'
    success_url = reverse_lazy ('reporte_listar')

class ReporteUpdate (UpdateView):
    models = Reporte
    form_class = ReporteForm
    template_name = 'reporte/reporte_form.html'
    success_url = reverse_lazy ('reporte_listar')
    def get_queryset(self): 
        return Reporte.objects.all()

class ReporteDelete (DeleteView):
    model = Reporte
    template_name = 'reporte/reporte_delete.html'
    success_url = reverse_lazy ('reporte_listar')

def profile (request):
    args = {'user': request.user}
    return render()
    return render(request, 'base/base.html',args)
