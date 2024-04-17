from django.urls import path
from . import views

urlpatterns = [
   path('novo_servico/', views.novo_servico, name="novo_servico"),
   path('listar_servico/', views.listar_servico, name="listar_servico"),
   path('servicos/<str:identificador>/', views.servico, name="servico"),
   #path('servicos', views.servico, name="servicos"),
   path('gerar_os/<str:identificador>', views.gerar_os, name="gerar_os"),
   #path('gerar_os/', views.gerar_os, name="gerar_os"),
   path('servico_adicional/', views.servico_adicional, name="servico_adicional")
]