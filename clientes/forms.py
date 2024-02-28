from django import forms
from django.core.validators import RegexValidator, ValidationError, EmailValidator
from .models import Cliente, Estado, Cidade, Bairro, Propriedade


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nome', 'sigla']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
            'origin_page': forms.HiddenInput()  # Mantendo o campo oculto como está
        }
        origin_page = forms.CharField(widget=forms.HiddenInput(), initial='cadastro_cliente')


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome', 'estado']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'origin_page': forms.HiddenInput()
        }
        origin_page = forms.CharField(widget=forms.HiddenInput(), initial='cadastro_cliente')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordena as opções de estado por nome na ordem alfabética
        self.fields['estado'].queryset = self.fields['estado'].queryset.order_by('nome')

class BairroForm(forms.ModelForm):
    class Meta:
        model = Bairro
        fields = ['nome', 'cidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
            'origin_page': forms.HiddenInput()
        }
        origin_page = forms.CharField(widget=forms.HiddenInput(), initial='cadastro_cliente')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordena as opções de cidade por nome na ordem alfabética
        self.fields['cidade'].queryset = self.fields['cidade'].queryset.order_by('nome')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Use '__all__' para incluir todos os campos do modelo no formulário
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
            'bairro': forms.Select(attrs={'class': 'form-control'}),
            'ponto_referencia': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_cliente': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['cep'] = forms.CharField(
            max_length=9, 
            validators=[RegexValidator(regex=r'^\d{5}-\d{3}$', message='CEP deve seguir o formato 12345-678.')],
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        self.fields['telefone_fixo'] = forms.CharField(
            required=False, 
            validators=[RegexValidator(regex=r'^\(\d{2}\) \d{4,5}-\d{4}$',message='Telefone fixo deve seguir o formato (xx) xxxx-xxxx ou (xx) xxxxx-xxxx.')],
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )

        self.fields['numero_celular'] = forms.CharField(
            required=False, 
            validators=[RegexValidator(regex=r'^\(\d{2}\) \d{5}-\d{4}$',message='Número de celular deve seguir o formato (xx) xxxxx-xxxx.')],
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )

        self.fields['email'] = forms.CharField(
            required=False, 
            validators=[EmailValidator(message='E-mail deve ser válido.')],
            widget=forms.EmailInput(attrs={'class': 'form-control'})
        )

        self.fields['cnpj'] = forms.CharField(
            required=False, 
            validators=[RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', message='CNPJ deve seguir o formato 12.345.678/9012-34.') ],
            widget=forms.TextInput(attrs={'class': 'form-control'}),
            initial=None  # Se você quiser definir um valor inicial
        )

        self.fields['cpf'] = forms.CharField(
            required=False, 
            validators=[RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',message='CPF deve seguir o formato 123.456.789-01.')],
            widget=forms.TextInput(attrs={'class': 'form-control'}),
            initial=None
        )
        cidades = Cidade.objects.values_list('id', 'nome')
        bairros = Bairro.objects.values_list('id', 'nome')

        self.fields['cidade'].choices = [('', 'Escolha uma cidade')] + list(cidades)
        self.fields['bairro'].choices = [('', 'Escolha um bairro')] + list(bairros)
        self.fields['estado'].queryset = self.fields['estado'].queryset.order_by('nome')

        # Adicione aqui a lógica para imprimir as opções de Cidade e Bairro
        print('Opções de Cidade:', list(Cidade.objects.values_list('id', 'nome')))
        print('Opções de Bairro:', list(Bairro.objects.values_list('id', 'nome')))

    def clean(self):
        cleaned_data = super().clean()
        tipo_cliente = cleaned_data.get('tipo_cliente')
        cidade = cleaned_data.get('cidade')
        bairro = cleaned_data.get('bairro')

        if tipo_cliente == 'PJ' and not cleaned_data.get('cnpj'):
            raise ValidationError({'cnpj': 'CNPJ é obrigatório para Pessoa Jurídica.'})
        elif tipo_cliente == 'PF' and not cleaned_data.get('cpf'):
            raise ValidationError({'cpf': 'CPF é obrigatório para Pessoa Física.'})


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

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        if cnpj.strip() == '':
            return None  # Permitir CNPJ vazio
        return cnpj

    def savecnpj(self, commit=True):
        instance = super().save(commit=False)
        cnpj = self.cleaned_data['cnpj']
        if cnpj == '':
            instance.cnpj = None  # Definir como None se o campo for vazio
        if commit:
            instance.save()
        return instance

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if cpf.strip() == '':
            return None  # Permitir CNPJ vazio
        return cpf

    def savecpf(self, commit=True):
        instance = super().save(commit=False)
        cpf = self.cleaned_data['cpf']
        if cpf == '':
            instance.cpf = None  # Definir como None se o campo for vazio
        if commit:
            instance.save()
        return instance

class PropriedadeForm(forms.ModelForm):
    class Meta:
        model = Propriedade
        fields = ['cliente', 'propriedade', 'area_instalacao', 'consumo', 'tipo_telhado', 'latitude', 'longitude']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'propriedade': forms.Select(attrs={'class': 'form-control'}),
            'area_instalacao': forms.NumberInput(attrs={'class': 'form-control'}),
            'consumo': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_telhado': forms.Select(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
        }