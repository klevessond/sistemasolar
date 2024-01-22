from django.urls import path
from clientes.views import clientes, novo_cliente, selecao_estado,load_estados

urlpatterns = [
        path('clientes', clientes, name='clientes'),
        path('novo_cliente', novo_cliente, name='novo_cliente'),
        path('selecao_estado', selecao_estado, name='selecao_estado'),
        path('ajax_load_estados', load_estados, name='ajax_load_estados'),
]
