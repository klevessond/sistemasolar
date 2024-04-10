from django.urls import path
from .views import criar_orcamento, detalhar_orcamento, orcamentos, propriedades_por_cliente

urlpatterns = [
    path('orcamentos/', orcamentos, name='orcamentos'),
    path('criar_orcamento/', criar_orcamento, name='criar_orcamento'),
    path('criar_orcamento/<int:cliente_id>', criar_orcamento, name='criar_orcamento_com_cliente'),
    path('detalhar_orcamento/<int:orcamento_id>', detalhar_orcamento, name='detalhar_orcamento'),
    path('ajax/propriedades_por_cliente/<int:cliente_id>/', propriedades_por_cliente, name='propriedades_por_cliente'),
    # Outras URLs conforme necessário
]
