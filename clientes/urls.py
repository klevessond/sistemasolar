from django.urls import path
from clientes.views import clientes, cadastro_cliente, get_cidades, get_bairros, cadastro_estado,cadastro_cidade, cadastro_bairro, editar_cliente
from clientes.views import cadastro_propriedade, detalhar_cliente
from . import views

urlpatterns = [
        path('clientes/', clientes, name='clientes'),
        path('cadastro_cliente', cadastro_cliente, name='cadastro_cliente'),
        path('ajax/get_cidades/', get_cidades, name='get_cidades'),
        path('ajax/get_bairros/', get_bairros, name='get_bairros'),
        path('cadastro_estado/', cadastro_estado, name='cadastro_estado'),
        path('cadastro_cidade/', cadastro_cidade, name='cadastro_cidade'),
        path('cadastro_bairro/', cadastro_bairro, name='cadastro_bairro'),
        path('editar_cliente/<int:cliente_id>', editar_cliente, name='editar_cliente'),
        path('cadastro_propriedade/<int:cliente_id>', cadastro_propriedade, name='cadastro_propriedade'),
        path('detalhar_cliente/<int:cliente_id>', detalhar_cliente, name='detalhar_cliente'),


]
