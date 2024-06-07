from django.db.models.signals import post_save
from django.dispatch import receiver
from clientes.models import Cliente
from .models import Orcamento

@receiver(post_save, sender=Cliente)
def sync_titularidade_to_orcamento(sender, instance, **kwargs):
    Orcamento.objects.filter(cliente=instance).update(titularidade=instance.titularidade)

@receiver(post_save, sender=Orcamento)
def sync_titularidade_to_cliente(sender, instance, **kwargs):
    cliente = instance.cliente
    if cliente.titularidade != instance.titularidade:
        cliente.titularidade = instance.titularidade
        cliente.save()