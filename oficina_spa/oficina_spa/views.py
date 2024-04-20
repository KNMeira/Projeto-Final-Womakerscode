from django.views.generic import ListView
from clientes.models import Cliente

class HistoricoClientesView(ListView):
    model = Cliente
    template_name = 'historico.html'
    context_object_name = 'clientes'  

    def get_queryset(self):
        return Cliente.objects.prefetch_related('carro_set', 'carro_set__servico_set')