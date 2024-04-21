from django.contrib import admin
from django.urls import path, include
from servicos import views as servicos_views
from clientes import views as clientes_views
from oficina_spa.oficina_spa import views as main_views
from oficina_spa.oficina_spa.views import HistoricoClientesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('servicos/', include('servicos.urls')),
    path('', servicos_views.login, name='login'),
    path('cadastro/', servicos_views.cadastro, name='cadastro'),
    path('gerenciamentoPerfil/', servicos_views.gerenciamentoPerfil, name='gerenciamentoPerfil'),
    path('historico/', HistoricoClientesView.as_view(), name='historico'),
]
