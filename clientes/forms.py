from django import forms
from django.core.validators import RegexValidator, ValidationError, EmailValidator
from .models import Cliente, Cidade, Bairro

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

        if tipo_cliente == 'PJ' and not cleaned_data.get('cnpj'):
            raise ValidationError({'cnpj': 'CNPJ é obrigatório para Pessoa Jurídica.'})
        elif tipo_cliente == 'PF' and not cleaned_data.get('cpf'):
            raise ValidationError({'cpf': 'CPF é obrigatório para Pessoa Física.'})

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['cidade'].queryset = Cidade.objects.none()
        self.fields['bairro'].queryset = Bairro.objects.none()
