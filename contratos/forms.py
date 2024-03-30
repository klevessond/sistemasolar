from django import forms
from .models import Orcamento
from clientes.models import Propriedade

class OrcamentoForm(forms.ModelForm):
    propriedade = forms.ModelChoiceField(queryset=Propriedade.objects.none())

    class Meta:
        model = Orcamento
        fields = ['cliente', 'propriedade', 'consumo', 'energia_gerada', 'numero_painel', 'painel_solar', 'numero_inversor', 'inversor', 'espaco_disponivel', 'tempo_garantia', 'valor_orcamento']

    def __init__(self, *args, **kwargs):
        cliente_id = kwargs.pop('cliente_id', None)
        super().__init__(*args, **kwargs)
        if cliente_id:
            self.fields['propriedade'].queryset = Propriedade.objects.filter(cliente_id=cliente_id)