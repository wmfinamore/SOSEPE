from django.db import models
from apps.core.models import Auditoria
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# TODO: Implementar validação para usar apenas CPF ou CNPJ
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

    def clean(self):
        if self.cpf is not None \
                and self.cnpj is not None:
            raise ValidationError(_('Defina apenas um documento para o cliente: CPF ou CNPJ'))
        if self.cpf is None \
                and self.cnpj is None:
            raise ValidationError(_('Defina pelo menos um documento para o cliente: CPF ou CNPJ'))
