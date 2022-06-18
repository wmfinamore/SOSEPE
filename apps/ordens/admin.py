from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import OrdemServico, StatusOrdemServico
from .forms import OrdermServicoForm


class OrdemServicoAdmin(SimpleHistoryAdmin):
    form = OrdermServicoForm
    list_display = ['numero', 'pedido', 'cliente', 'descricao', 'data_entrega']
    search_fields = ['numero', 'pedido', 'cliente', 'descricao', 'data_entrega']
    autocomplete_fields = ['cliente']


admin.site.register(OrdemServico, OrdemServicoAdmin)
admin.site.register(StatusOrdemServico)
