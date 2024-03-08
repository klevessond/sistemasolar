from django import forms
from .models import PainelSolar, Inversor, Modelousina

class PainelSolarForm(forms.ModelForm):
    class Meta:
        model = PainelSolar
        fields = '__all__'
        widgets = {
            'fabricante': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidade_watt': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class InversorForm(forms.ModelForm):
    class Meta:
        model = Inversor
        fields = '__all__'
        widgets = {
            'fabricante': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidade_watt': forms.NumberInput(attrs={'class': 'form-control'}),
            'tensao_entrada_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'tensao_saida': forms.NumberInput(attrs={'class': 'form-control'}),
            'eficiencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'compatibilidade': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class UsinaForm(forms.ModelForm):
    class Meta:
        model = Modelousina
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'painel_solar': forms.Select(attrs={'class': 'form-control'}),
            'painel_quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'inversor': forms.Select(attrs={'class': 'form-control'}),
            # Adicione outros campos aqui, se necessário, seguindo o mesmo padrão.
        }