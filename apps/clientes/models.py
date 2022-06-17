from django.db import models
from apps.core.models import Auditoria
from django_cpf_cnpj.fields import CPFField, CNPJField


# TODO: Definir Verbose Names
class Cliente(Auditoria):
    nome = models.CharField(max_length=250, null=True, blank=True, verbose_name='Nome')
    cpf = CPFField(masked=True, null=True, blank=True, verbose_name='CPF')
    cnpj = CNPJField(masked=True, null=True, blank=True, verbose_name='CNPJ')

    def __str__(self):
        if self.cpf:
            return str(self.cpf) + " - " + str(self.nome)
        elif self.cnpj:
            return str(self.cnpj) + " - " + str(self.nome)
        else:
            return str(self.nome)
