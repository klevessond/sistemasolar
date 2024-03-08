from django.contrib import admin
from clientes.models import Cliente, Estado, Cidade, Bairro, Propriedade

admin.site.register(Cliente)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Propriedade)

