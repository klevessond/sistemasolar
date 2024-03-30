from django.urls import path
from .views import criar_orcamento

urlpatterns = [
    path('orcamento/criar/', criar_orcamento, name='criar_orcamento'),
    path('orcamento/criar/<int:cliente_id>/', criar_orcamento, name='criar_orcamento_com_cliente'),
    # Outras URLs conforme necessário
]
