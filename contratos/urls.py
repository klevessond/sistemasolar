from django.urls import path
from .views import criar_orcamento

urlpatterns = [
    path('criar_orcamento/', criar_orcamento, name='criar_orcamento'),
    # Inclua outras URLs aqui
]
