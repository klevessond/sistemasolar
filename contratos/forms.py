from django import forms
from .models import Orcamento

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['cliente', 'consumo', 'energia_gerada', 'numero_painel', 'painel_solar', 'numero_inversor', 'inversor', 'espaco_disponivel', 'tempo_garantia', 'valor_orcamento']