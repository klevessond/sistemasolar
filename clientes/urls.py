from django.urls import path
from clientes.views import clientes, novo_cliente

urlpatterns = [
        path('clientes', clientes, name='clientes'),
        path('novo_cliente', novo_cliente, name='novo_cliente'),
]
