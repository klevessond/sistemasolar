from django import forms
from django.core.validators import RegexValidator, ValidationError, EmailValidator
from .models import Cliente, Estado, Cidade, Bairro


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nome', 'sigla']
        origin_page = forms.CharField(widget=forms.HiddenInput(), initial='cadastro_cliente')

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome', 'estado']
        origin_page = forms.CharField(widget=forms.HiddenInput(), initial='cadastro_cliente')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordena as opções de estado por nome na ordem alfabética
        self.fields['estado'].queryset = self.fields['estado'].queryset.order_by('nome')

class BairroForm(forms.ModelForm):
    class Meta:
        model = Bairro
        fields = ['nome', 'cidade']
        origin_page = forms.CharField(widget=forms.HiddenInput(), initial='cadastro_cliente')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordena as opções de cidade por nome na ordem alfabética
        self.fields['cidade'].queryset = self.fields['cidade'].queryset.order_by('nome')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Use '__all__' para incluir todos os campos do modelo no formulário

    # Adicione validadores adicionais ou personalizações aqui
    cep = forms.CharField(max_length=9, validators=[RegexValidator(
        regex=r'^\d{5}-\d{3}$',
        message='CEP deve seguir o formato 12345-678.',
        code='invalid_cep'
    )])

    telefone_fixo = forms.CharField(max_length=15, required=False, validators=[RegexValidator(
        regex=r'^\(\d{2}\) \d{4,5}-\d{4}$',
        message='Telefone fixo deve seguir o formato (xx) xxxx-xxxx ou (xx) xxxxx-xxxx.',
        code='invalid_telefone_fixo'
    )])

    numero_celular = forms.CharField(max_length=15, required=False, validators=[RegexValidator(
        regex=r'^\(\d{2}\) \d{5}-\d{4}$',
        message='Número de celular deve seguir o formato (xx) xxxxx-xxxx.',
        code='invalid_celular'
    )])

    email = forms.CharField(max_length=100, required=False, validators=[EmailValidator(
        message='E-mail deve ser válido.',
        code='invalid_email'
    )])

    cnpj = forms.CharField(max_length=18, required=False, validators=[RegexValidator(
        regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$',
        message='CNPJ deve seguir o formato 12.345.678/9012-34.',
        code='invalid_cnpj'
    )])

    cpf = forms.CharField(max_length=14, required=False, validators=[RegexValidator(
        regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
        message='CPF deve seguir o formato 123.456.789-01.',
        code='invalid_cpf'
    )])

    def clean(self):
        cleaned_data = super().clean()
        tipo_cliente = cleaned_data.get('tipo_cliente')
        cidade = cleaned_data.get('cidade')
        bairro = cleaned_data.get('bairro')

        if tipo_cliente == 'PJ' and not cleaned_data.get('cnpj'):
            raise ValidationError({'cnpj': 'CNPJ é obrigatório para Pessoa Jurídica.'})
        elif tipo_cliente == 'PF' and not cleaned_data.get('cpf'):
            raise ValidationError({'cpf': 'CPF é obrigatório para Pessoa Física.'})

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        cidades = Cidade.objects.values_list('id', 'nome')
        bairros = Bairro.objects.values_list('id', 'nome')

        self.fields['cidade'].choices = [('', 'Escolha uma cidade')] + list(cidades)
        self.fields['bairro'].choices = [('', 'Escolha um bairro')] + list(bairros)

        # Adicione aqui a lógica para imprimir as opções de Cidade e Bairro
        print('Opções de Cidade:', list(Cidade.objects.values_list('id', 'nome')))
        print('Opções de Bairro:', list(Bairro.objects.values_list('id', 'nome')))

    def clean_cidade(self):
        cidade = self.cleaned_data['cidade']
        if not cidade:
            raise ValidationError('Escolha uma cidade válida.')
        return cidade

    def clean_bairro(self):
        bairro = self.cleaned_data['bairro']
        if not bairro:
            raise ValidationError('Escolha um bairro válido.')
        return bairro
