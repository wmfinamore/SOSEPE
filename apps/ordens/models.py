from django.db import models
from apps.core.models import Auditoria
from apps.clientes.models import Cliente


# TODO: definir verbose names
# TODO: Criar model para Status do Pedido
class OrdemServico(Auditoria):
    numero = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='Número da O.S.')
    pedido = models.CharField(max_length=50, null=True, blank=True, verbose_name='Número do pedido')
    data_pedido = models.DateField(null=True, blank=True, verbose_name='data do pedido')
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=250, null=True, blank=True, verbose_name='Descrição')
    quantidade = models.PositiveIntegerField(default=0)
    valor = models.DecimalField(max_digits=20, decimal_places=2, default=0.0, verbose_name='R$')
    imposto = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    data_entrega = models.DateField(null=True, blank=True, verbose_name='Data da Entrega')
    observacao = models.TextField(null=True, blank=True, verbose_name='Observação')
    nota_fiscal = models.CharField(max_length=10, null=True, blank=True, verbose_name='Nota Fiscal')
    data_entrega_real = models.DateField(null=True, blank=True, verbose_name='Data de Entrega Real')

    def __str__(self):
        return str(self.numero) + " - " + str(self.descricao)

    @property
    def valor_total(self):
        return self.valor + self.imposto

    class Meta:
        ordering = ['data_entrega']
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'
