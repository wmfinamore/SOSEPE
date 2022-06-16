from django.db import models
from apps.core.models import Auditoria
from apps.clientes.models import Cliente


class OrdemServico(Auditoria):
    numero = models.PositiveBigIntegerField(null=True, blank=True)
    pedido = models.CharField(max_length=50, null=True, blank=True)
    data_pedido = models.DateField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True)
    descricao = models.CharField(max_length=250, null=True, blank=True)
    quantidade = models.PositiveIntegerField(default=0)
    valor = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    imposto = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    data_entrega = models.DateField(null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)
    nota_fiscal = models.CharField(max_length=10, null=True, blank=True)
    data_entrega_real = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.numero) + " - " + str(self.descricao)
