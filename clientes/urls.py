from django.urls import path
from clientes.views import clientes

urlpatterns = [
        path('clientes', clientes, name='clientes')
]
