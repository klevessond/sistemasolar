from django.urls import path
from clientes.views import clientes, novo_cliente, get_cidades, get_bairros

urlpatterns = [
        path('clientes', clientes, name='clientes'),
        path('novo_cliente', novo_cliente, name='novo_cliente'),
        path('ajax/get_cidades/', get_cidades, name='get_cidades'),
        path('ajax/get_bairros/', get_bairros, name='get_bairros'),

]
