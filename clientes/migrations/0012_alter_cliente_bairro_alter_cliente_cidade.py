# Generated by Django 4.1 on 2024-01-11 19:49

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_rename_cidade_bairro_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='bairro',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='cidade', chained_model_field='cidade', null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.bairro'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cidade',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='estado', chained_model_field='estado', null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.cidade'),
        ),
    ]