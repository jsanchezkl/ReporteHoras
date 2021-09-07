from django.urls import path, include
from apps.actividad.views import ActividadCreate, index, ActividadList,ActividadUpdate,ActividadDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
     path('', index, name= 'index'),
     path('nuevo/', login_required(ActividadCreate.as_view()), name= 'actividad_crear'),
     path('listar/', login_required(ActividadList.as_view()), name= 'actividad_listar'),
     path('editar/<int:pk>/', login_required(ActividadUpdate.as_view()), name= 'actividad_editar'),
     path('eliminar/<int:pk>/', login_required(ActividadDelete.as_view()), name= 'actividad_eliminar'),
     
]
