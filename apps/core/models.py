from django.db import models
from simple_history.models import HistoricalRecords


class Auditoria(models.Model):
    data_inclusao = models.DateField(auto_now_add=True)
    hora_inclusao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    hora_alteracao = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        abstract = True
