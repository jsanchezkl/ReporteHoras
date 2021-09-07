from django.urls import path
from django.urls import path, include
from apps.campania.views import index
from apps.campania.views import index
from django.contrib.auth.decorators import login_required
from apps.campania.views import CampaniaList, CampaniaCreate

urlpatterns = [
     path('', index, name= 'index'),
     path('nuevo/', login_required(CampaniaCreate.as_view()), name= 'campania_crear'),
     path('listar/', login_required(CampaniaList.as_view()), name= 'campania_listar'),
]
