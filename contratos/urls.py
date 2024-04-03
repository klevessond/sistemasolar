from django.urls import path
from .views import criar_orcamento, detalhar_orcamento,orcamentos

urlpatterns = [
    path('orcamentos/', orcamentos, name='orcamentos'),
    path('criar_orcamento/', criar_orcamento, name='criar_orcamento'),
    path('criar_orcamento/<int:cliente_id>/', criar_orcamento, name='criar_orcamento_com_cliente'),
    path('detalhar_orcamento/<int:status_id>/', detalhar_orcamento, name='detalhar_orcamento'),
    # Outras URLs conforme necessário
]
