from django.urls import path
from .views import ListarServicios, ListarServiciosPorCategoria


name_app = 'catalogos'
  
urlpatterns = [
    path('', ListarServicios.as_view(), name='listar_servicios'),
    path('servicios/categoria/<int:categoria_id>/', ListarServiciosPorCategoria.as_view(), name='listar_servicios_por_categoria'),
]