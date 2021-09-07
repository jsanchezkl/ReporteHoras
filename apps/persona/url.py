from django.urls import path
from django.urls import path, include
from apps.persona.views import index
from django.contrib.auth.decorators import login_required
from apps.persona.views import PersonaList, PersonaCreate

urlpatterns = [
     path('', index, name= 'index'),
     path('nuevo/', login_required(PersonaCreate.as_view()), name= 'persona_crear'),
     path('listar/', login_required(PersonaList.as_view()), name= 'persona_listar'),
]
