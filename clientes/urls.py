from django.urls import path
from clientes.views import clientes, cadastro_cliente, get_cidades, get_bairros, cadastro_estado, cadastro_cidade, cadastro_bairro

urlpatterns = [
        path('clientes/', clientes, name='clientes'),
        path('cadastro_cliente', cadastro_cliente, name='cadastro_cliente'),
        path('ajax/get_cidades/', get_cidades, name='get_cidades'),
        path('ajax/get_bairros/', get_bairros, name='get_bairros'),
        path('cadastro_estado/', cadastro_estado, name='cadastro_estado'),
        path('cadastro_cidade/', cadastro_cidade, name='cadastro_cidade'),
        path('cadastro_bairro/', cadastro_bairro, name='cadastro_bairro'),

]
