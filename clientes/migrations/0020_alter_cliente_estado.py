# Generated by Django 4.1 on 2024-01-24 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0019_alter_cliente_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.estado'),
        ),
    ]
