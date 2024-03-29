from django.db import models
# Importando os modelos necessários
from clientes.models import Cliente
from usinas.models import PainelSolar, Inversor

class Orcamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    consumo = models.IntegerField()
    energia_gerada = models.IntegerField()
    numero_painel = models.IntegerField()
    painel_solar = models.ForeignKey(PainelSolar, on_delete=models.CASCADE)
    numero_inversor = models.IntegerField()
    inversor = models.ForeignKey(Inversor, on_delete=models.CASCADE)
    espaco_disponivel = models.DecimalField(max_digits=10, decimal_places=2)  # Até 10 dígitos no total, com 2 casas decimais
    tempo_garantia = models.IntegerField()
    valor_orcamento = models.IntegerField()

    def __str__(self):
        return f"Orçamento {self.id} - Cliente {self.cliente.nome_completo}"