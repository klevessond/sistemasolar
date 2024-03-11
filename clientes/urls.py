from django.urls import path
from clientes.views import clientes, cadastro_cliente, get_cidades, get_bairros, cadastro_estado,cadastro_cidade, cadastro_bairro, editar_cliente
from clientes.views import cadastro_propriedade, detalhar_cliente,detalhar_estado,detalhar_cidade,detalhar_bairro,editar_estado,editar_cidade,editar_bairro
from clientes.views import estados, cidades, bairros,gerenciar_endereco
urlpatterns = [
        path('clientes/', clientes, name='clientes'),
        path('estados/', estados, name='estados'),
        path('cidades/', cidades, name='cidades'),
        path('bairros/', bairros, name='bairros'),
        path('cadastro_cliente', cadastro_cliente, name='cadastro_cliente'),
        path('cadastro_propriedade/<int:cliente_id>', cadastro_propriedade, name='cadastro_propriedade'),
        path('ajax/get_cidades/', get_cidades, name='get_cidades'),
        path('ajax/get_bairros/', get_bairros, name='get_bairros'),
        path('cadastro_estado/', cadastro_estado, name='cadastro_estado'),
        path('cadastro_cidade/', cadastro_cidade, name='cadastro_cidade'),
        path('cadastro_bairro/', cadastro_bairro, name='cadastro_bairro'),
        path('editar_cliente/<int:cliente_id>', editar_cliente, name='editar_cliente'),
        path('editar_estado/<int:estado_id>', editar_estado, name='editar_estado'),
        path('editar_cidade/<int:cidade_id>', editar_cidade, name='editar_cidade'),
        path('editar_bairro/<int:bairro_id>', editar_bairro, name='editar_bairro'),
        path('detalhar_cliente/<int:cliente_id>', detalhar_cliente, name='detalhar_cliente'),
        path('detalhar_estado/<int:estado_id>', detalhar_estado, name='detalhar_estado'),
        path('detalhar_cidade/<int:cidade_id>', detalhar_cidade, name='detalhar_cidade'),
        path('detalhar_bairro/<int:bairro_id>', detalhar_bairro, name='detalhar_bairro'),
        path('gerenciar_endereco/', gerenciar_endereco, name='gerenciar_endereco'),


]
