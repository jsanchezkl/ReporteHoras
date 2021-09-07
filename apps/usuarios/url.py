from django.urls import path
from django.urls import path, include
from apps.usuarios.views import RegistroUsuario

urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name= 'registrar'),
]
