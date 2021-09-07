"""proy_horas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import login
from django.contrib.auth.views import *
from django.contrib.auth import views as auth_views #import this
#from . import views
#from django.contrib.auth.views import LoginView, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('actividad/', include ('apps.actividad.url')),
    path('campania/', include ('apps.campania.url')),
    path('persona/', include ('apps.persona.url')),
    path('reporte/', include ('apps.reporte.url')),
    path('usuario/', include ('apps.usuarios.url')),
    #path("password_reset", views.password_reset_request, name="password_reset"),
    path('', LoginView.as_view(template_name='index.html'), name='login'),
    path('accounts/login/', LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('reset/password_reset/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),      


    
   
    
]
