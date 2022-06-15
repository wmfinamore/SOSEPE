from django.db import models
from apps.core.models import Auditoria
from django_cpf_cnpj.fields import CPFField, CNPJField


class Cliente(Auditoria):
    nome = models.CharField(max_length=250, null=True, blank=True)
    cpf = CPFField(masked=True, null=True, blank=True)
    cnpj = CNPJField(masked=True, null=True, blank=True)

    def __str__(self):
        if self.cpf:
            return str(self.cpf) + " - " + str(self.nome)
        elif self.cnpj:
            return str(self.cnpj) + " - " + str(self.nome)
        else:
            return str(self.nome)
