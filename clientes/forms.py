from django import forms
from django.core.validators import RegexValidator, ValidationError, EmailValidator
from .models import Cliente, Estado, Cidade, Bairro

class ClienteForm(forms.ModelForm):
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), required=True, label='Estado')
    cidade = forms.ModelChoiceField(queryset=Cidade.objects.none(), required=True, label='Cidade')
    bairro = forms.ModelChoiceField(queryset=Bairro.objects.none(), required=True, label='Bairro')

    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        # Adicione classes CSS se desejar
        self.fields['estado'].widget.attrs['class'] = 'estado-select'
        self.fields['cidade'].widget.attrs['class'] = 'cidade-select'
        self.fields['bairro'].widget.attrs['class'] = 'bairro-select'

        # Adicione um evento onchange ao campo estado
        self.fields['estado'].widget.attrs['onchange'] = 'update_cidades()'

    def clean(self):
        cleaned_data = super().clean()
        estado = cleaned_data.get('estado')
        cidade = cleaned_data.get('cidade')

        # Atualize as opções do campo cidade com base no estado selecionado
        if estado:
            self.fields['cidade'].queryset = Cidade.objects.filter(estado=estado)
        else:
            self.fields['cidade'].queryset = Cidade.objects.none()

        # Atualize as opções do campo bairro com base na cidade selecionada
        if cidade:
            self.fields['bairro'].queryset = Bairro.objects.filter(cidade=cidade)
        else:
            self.fields['bairro'].queryset = Bairro.objects.none()

        return cleaned_data

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
