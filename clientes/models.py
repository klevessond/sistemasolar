from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator

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

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=100, blank=False, null=False)
    rua = models.CharField(max_length=100, blank=False, null=False)
    numero = models.IntegerField(blank=False, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, blank=False, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, blank=False, null=True)
    bairro = models.CharField(max_length=100, blank=False, null=False)

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
    cnpj = models.CharField(max_length=18, validators=[cnpj_validator], unique=True, blank=True, null=True)

    cpf_validator = RegexValidator(
        regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
        message='CPF deve seguir o formato 123.456.789-01.',
        code='invalid_cpf'
    )
    cpf = models.CharField(max_length=14, validators=[cpf_validator], unique=True, blank=True, null=True)

    def clean(self):
        if self.tipo_cliente == 'PJ' and not self.cnpj:
            raise ValidationError({'cnpj': 'CNPJ é obrigatório para Pessoa Jurídica.'})
        elif self.tipo_cliente == 'PF' and not self.cpf:
            raise ValidationError({'cpf': 'CPF é obrigatório para Pessoa Física.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_completo
