from django import forms
from .models import Orcamento, Propriedade, TipoPagamento
from django.contrib.admin.widgets import AdminDateWidget



class TipoPagamentoForm(forms.ModelForm):
    class Meta:
        model = TipoPagamento
        fields = ['nome']


class OrcamentoForm(forms.ModelForm):

    tipos_pagamento = forms.ModelMultipleChoiceField(
        queryset=TipoPagamento.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'related-widget-wrapper', 'data-model-ref': 'tipo pagamento'}),
        required=True
    )
    tempo_garantia = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Orcamento
        fields = ['cliente', 'propriedade', 'consumo', 'painel_solar', 'numero_painel', 'valor_unitario_painel', 'inversor', 'numero_inversor',
                   'valor_unitario_inversor', 'energia_gerada', 'espaco_disponivel', 'tempo_garantia', 'valor_orcamento', 'status', 'info_adicionais',
                   'titularidade','valor_maodeobra']

    def __init__(self, *args, **kwargs):
        cliente_id = kwargs.pop('cliente_id', None)
        super(OrcamentoForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            cliente = kwargs['instance'].cliente
            self.fields['propriedade'].queryset = Propriedade.objects.filter(cliente=cliente)
        elif 'data' in kwargs:
            cliente_id = kwargs['data'].get('cliente')
            if cliente_id:
                self.fields['propriedade'].queryset = Propriedade.objects.filter(cliente_id=cliente_id)
            else:
                self.fields['propriedade'].queryset = Propriedade.objects.none()
