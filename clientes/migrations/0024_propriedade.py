# Generated by Django 4.1 on 2024-02-28 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0023_alter_cliente_cnpj_alter_cliente_cpf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propriedade', models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial'), ('industrial', 'Industrial')], max_length=50, verbose_name='Tipo de Propriedade')),
                ('area_instalacao', models.IntegerField(verbose_name='Área de Instalação')),
                ('consumo', models.IntegerField(verbose_name='Consumo Mensal')),
                ('tipo_telhado', models.CharField(choices=[('inclinado', 'Telhado Inclinado'), ('plano', 'Telhado Plano'), ('metal', 'Telhado de Metal')], max_length=50, verbose_name='Tipo de Telhado')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Propriedade',
                'verbose_name_plural': 'Propriedades',
            },
        ),
    ]