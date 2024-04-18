from django.contrib import admin
from django.urls import path, include
from servicos import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('servicos/', include('servicos.urls')),
    path('',views.login,name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('gerenciamentoPerfil/', views.gerenciamentoPerfil, name='gerenciamentoPerfil'),
]
