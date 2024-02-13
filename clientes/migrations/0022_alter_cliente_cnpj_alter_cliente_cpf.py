# Generated by Django 4.1 on 2024-02-08 01:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0021_alter_cliente_bairro_alter_cliente_cidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_cnpj', message='CNPJ deve seguir o formato 12.345.678/9012-34.', regex='^\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}$')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_cpf', message='CPF deve seguir o formato 123.456.789-01.', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')]),
        ),
    ]