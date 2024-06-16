from django.db import models
# Importando os modelos necessários
from clientes.models import Cliente, Propriedade
from usinas.models import PainelSolar, Inversor


class TipoPagamento(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Orcamento(models.Model):
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    propriedade = models.ForeignKey('clientes.Propriedade', on_delete=models.CASCADE, null=True, blank=True)
    consumo = models.IntegerField()
    energia_gerada = models.IntegerField()
    numero_painel = models.IntegerField()
    painel_solar = models.ForeignKey(PainelSolar, on_delete=models.CASCADE)
    numero_inversor = models.IntegerField()
    inversor = models.ForeignKey(Inversor, on_delete=models.CASCADE)
    espaco_disponivel = models.DecimalField(max_digits=10, decimal_places=2)  # Até 10 dígitos no total, com 2 casas decimais
    tempo_garantia = models.DateField()
    valor_orcamento = models.IntegerField()
    STATUS_CHOICES = [
        ('aberto', 'Em Aberto'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    ]
        
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberto')
    valor_unitario_painel = models.IntegerField(null=True, blank=True, verbose_name='Valor Unitário do Painel')
    valor_unitario_inversor = models.IntegerField(null=True, blank=True, verbose_name='Valor Unitário da Inversor')
    valor_maodeobra = models.IntegerField(null=True, blank=True, verbose_name='Valor mao de obra')    
    titularidade = models.BooleanField(default=True)  # Novo campo
    info_adicionais = models.TextField(null=True, blank=True, verbose_name='Informações Adicionais')
    tipos_pagamento = models.ManyToManyField(TipoPagamento, related_name='orcamentos')



    def __str__(self):
        return f"Orçamento {self.id} - {self.get_status_display()}"

    #def __str__(self):
     #   return f"Orçamento {self.id} - Cliente {self.cliente.nome_completo}"

