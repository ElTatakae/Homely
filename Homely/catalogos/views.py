from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Servicio

# Create your views here.
class ListarServicios(ListView):
    model = Servicio
    template_name = 'listar_servicios.html'
    context_object_name = 'servicios'
    paginate_by = 3
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))        
        return queryset
    
    
class ListarServiciosPorCategoria(ListView):
    template_name = 'listar_servicios.html'

    def get(self, request, *args, **kwargs):
        categoria_id = kwargs.get('categoria_id')
        servicios = Servicio.objects.filter(categoria=categoria_id)
        return render(request, self.template_name, {'servicios': servicios})