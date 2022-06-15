from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Cliente


class ClienteAdmin(SimpleHistoryAdmin):
    list_display = ['nome', 'cpf', 'cnpj']
    search_fields = ['nome', 'cpf', 'cnpj']


admin.site.register(Cliente, ClienteAdmin)
