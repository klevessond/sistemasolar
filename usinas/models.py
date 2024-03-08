from django.db import models
from clientes.models import Cliente

# Create your models here.
class PainelSolar(models.Model):
    fabricante = models.CharField(max_length=120, blank=False)
    modelo = models.CharField(max_length=120, blank=False)
    capacidade_watt = models.IntegerField(blank=False)


class Inversor(models.Model):
    TIPO_CHOICES = [
        ('string', 'String'),
        ('central', 'Central'),
        ('micro', 'Micro'),
    ]

    fabricante = models.CharField(max_length=120, blank=False)
    modelo = models.CharField(max_length=120, blank=False)
    capacidade_watt = models.IntegerField(blank=False)
    tensao_entrada_max = models.IntegerField(blank=False)
    tensao_saida = models.IntegerField(blank=False)
    eficiencia = models.IntegerField(blank=False)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES, blank=False)
    compatibilidade = models.TextField(max_length=500, blank=False)

class Modelousina(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    painel_solar = models.ForeignKey(PainelSolar, on_delete=models.CASCADE)
    painel_quantidade = models.IntegerField()
    inversor = models.ForeignKey(Inversor, on_delete=models.CASCADE)