from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import OrdemServico, StatusOrdemServico
from .forms import OrdermServicoForm


class OrdemServicoAdmin(SimpleHistoryAdmin):
    form = OrdermServicoForm
    list_display = ['numero', 'pedido', 'cliente', 'descricao', 'data_entrega']
    search_fields = ['numero', 'pedido', 'cliente', 'descricao', 'data_entrega']
    autocomplete_fields = ['cliente']
    fieldsets = (
        ('Identificação', {
            'fields': (
                ('numero', 'pedido', 'status'),
                ('cliente', 'data_pedido', 'data_entrega'),
            )
        }),
        ('Detalhes da O.S.', {
            'fields': (
                ('descricao', 'quantidade'),
                ('valor', 'imposto'),
                ('observacao',)
            )
        }),
        ('Finalização da O.S.', {
            'fields': (
                ('nota_fiscal', 'data_entrega_real')
            )
        })
    )


admin.site.register(OrdemServico, OrdemServicoAdmin)
admin.site.register(StatusOrdemServico)
