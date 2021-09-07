from django.urls import path
from django.urls import path, include
from apps.reporte.views import index
from apps.reporte.views import ReporteList, ReporteCreate, ReporteDelete, ReporteUpdate
from django.contrib.auth.decorators import login_required

urlpatterns = [
     path('', index, name= 'index'),
     path('nuevo/',login_required(ReporteCreate.as_view()), name= 'reporte_crear'),
     path('listar/', login_required(ReporteList.as_view()), name= 'reporte_listar'),
     path('editar/<int:pk>/', login_required(ReporteUpdate.as_view()), name= 'reporte_editar'),
     path('eliminar/<int:pk>/', login_required(ReporteDelete.as_view()), name= 'reporte_eliminar'),
]
