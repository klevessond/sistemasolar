# Generated by Django 5.0.1 on 2024-01-11 02:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_alter_cliente_bairro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='bairro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.bairro'),
        ),
    ]
