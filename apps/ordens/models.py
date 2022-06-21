from django.db import models
from apps.core.models import Auditoria
from apps.clientes.models import Cliente
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from config.settings import RISCO


# TODO: Criar incremento automático para número da O.S. com transação
class StatusOrdemServico(models.Model):
    status_ordem_servico = models.CharField(max_length=30, verbose_name='Status de O.S.', unique=True)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.status_ordem_servico)

    class Meta:
        verbose_name = 'Status de O.S.'
        verbose_name_plural = 'Status de O.S.'


class OrdemServico(Auditoria):
    numero = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='Número da O.S.')
    pedido = models.CharField(max_length=50, null=True, blank=True, verbose_name='Número do pedido')
    data_pedido = models.DateField(null=True, blank=True, verbose_name='data do pedido')
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.PROTECT)
    status = models.ForeignKey(StatusOrdemServico,on_delete=models.PROTECT, verbose_name='Status da O.S.')
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

    @property
    def situacao(self):
        if self.data_entrega is not None \
                and self.data_entrega_real is not None \
                and self.data_entrega_real > self.data_entrega:
            return 'Entregue com Atraso'
        elif self.data_entrega is not None \
                and self.data_entrega_real is not None \
                and self.data_entrega_real <= self.data_entrega:
            return 'Entregue no Prazo'
        elif self.data_entrega is not None \
                and self.data_entrega_real is None \
                and self.data_entrega < date.today():
            return 'Pedido Atrasado'
        elif self.data_entrega is not None \
                and self.data_entrega_real is None \
                and (self.data_entrega - date.today()).days <= RISCO:
            return 'Em risco de Atraso'
        else:
            return 'Em andamento'

    def clean(self):
        if self.data_entrega is not None \
                and self.data_pedido is not None \
                and self.data_entrega < self.data_pedido:
            raise ValidationError(_('Data de entrega não pode ser menor que a data do pedido.'))
        if self.data_entrega_real is not None \
                and self.data_pedido is not None \
                and self.data_entrega_real < self.data_pedido:
            raise ValidationError(_('Data de entrega real não pode ser menor que a data do pedido.'))

    def save(self, *args, **kwargs):
        if self.id:
            pass
        else:
            ordem = OrdemServico.objects.all().order_by('-numero').first()
            if ordem:
                self.numero = int(ordem.numero) + 1
            else:
                self.numero = 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['data_entrega']
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'
