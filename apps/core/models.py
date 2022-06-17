from django.db import models
from simple_history.models import HistoricalRecords


# TODO: Definir Verbose Names
class Auditoria(models.Model):
    data_inclusao = models.DateField(auto_now_add=True, verbose_name='Data de Inclusão')
    hora_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Hora de Inclusão')
    data_alteracao = models.DateField(auto_now=True, verbose_name='Data de Alteração')
    hora_alteracao = models.DateTimeField(auto_now=True, verbose_name='Hora de Alteração')
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
