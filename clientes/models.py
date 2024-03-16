from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator
from smart_selects.db_fields import ChainedForeignKey

class Estado(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.estado.sigla}"

class Bairro(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=100, blank=False, null=False)
    rua = models.CharField(max_length=100, blank=False, null=False)
    numero = models.IntegerField(blank=False, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, blank=False, null=True)
    cidade = ChainedForeignKey(Cidade, on_delete=models.SET_NULL, blank=False, null=True,
                                        chained_field="estado",
                                        chained_model_field="estado",
                                        show_all=False,
                                        auto_choose=True,
                                        sort=True)
    bairro = ChainedForeignKey(Bairro, on_delete=models.SET_NULL, blank=False, null=True,
                                chained_field="cidade",
                                chained_model_field="cidade",
                                show_all=False,
                                auto_choose=True,
                                sort=True)

    cep_validator = RegexValidator(
        regex=r'^\d{5}-\d{3}$',
        message='CEP deve seguir o formato 12345-678.',
        code='invalid_cep'
    )
    cep = models.CharField(max_length=9, validators=[cep_validator], blank=False, null=False)

    ponto_referencia = models.CharField(max_length=200, blank=True, null=True)

    telefone_fixo_validator = RegexValidator(
        regex=r'^\(\d{2}\) \d{4,5}-\d{4}$',
        message='Telefone fixo deve seguir o formato (xx) xxxx-xxxx ou (xx) xxxxx-xxxx.',
        code='invalid_telefone_fixo'
    )
    telefone_fixo = models.CharField(max_length=15, validators=[telefone_fixo_validator], blank=True, null=True)

    celular_validator = RegexValidator(
        regex=r'^\(\d{2}\) \d{5}-\d{4}$',
        message='Número de celular deve seguir o formato (xx) xxxxx-xxxx.',
        code='invalid_celular'
    )
    numero_celular = models.CharField(max_length=15, validators=[celular_validator], blank=True, null=True)

    email_validator = EmailValidator(message='E-mail deve ser válido.', code='invalid_email')
    email = models.CharField(max_length=100, validators=[email_validator], blank=True, null=True)

    TIPO_CLIENTE_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]
    tipo_cliente = models.CharField(max_length=50, choices=TIPO_CLIENTE_CHOICES, blank=False, null=False)

    cnpj_validator = RegexValidator(
        regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$',
        message='CNPJ deve seguir o formato 12.345.678/9012-34.',
        code='invalid_cnpj'
    )
    cnpj = models.CharField(max_length=18, validators=[cnpj_validator], unique=True, blank=True, null=True,default=None)

    cpf_validator = RegexValidator(
        regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
        message='CPF deve seguir o formato 123.456.789-01.',
        code='invalid_cpf'
    )
    cpf = models.CharField(max_length=14, validators=[cpf_validator], unique=True, blank=True, null=True,default=None)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_completo

class Propriedade(models.Model):
    # Definindo as escolhas para o campo 'propriedade'
    PROPRIEDADE_CHOICES = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
        ('industrial', 'Industrial'),
        ('fazenda', 'Fazenda'),
    ]

    # Definindo as escolhas para o campo 'tipo_telhado'
    TIPO_TELHADO_CHOICES = [
        ('inclinado', 'Telhado Inclinado'),
        ('plano', 'Telhado Plano'),
        ('metal', 'Telhado de Metal'),
        ('estrutura elevada', 'Estrutura Elevada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    propriedade = models.CharField(max_length=50, choices=PROPRIEDADE_CHOICES, verbose_name='Tipo de Propriedade')
    area_instalacao = models.IntegerField(verbose_name='Área de Instalação')
    consumo = models.IntegerField(verbose_name='Consumo Mensal')
    tipo_telhado = models.CharField(max_length=50, choices=TIPO_TELHADO_CHOICES, verbose_name='Tipo de Telhado')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Latitude')
    longitude = models.FloatField(null=True, blank=True, verbose_name='Longitude')

    def __str__(self):
        return f"{self.get_propriedade_display()} - {self.cliente.nome_completo}"

    class Meta:
        verbose_name = 'Propriedade'
        verbose_name_plural = 'Propriedades'
