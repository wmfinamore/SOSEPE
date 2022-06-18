from django.contrib import admin
from django.utils.html import format_html
from simple_history.admin import SimpleHistoryAdmin
from .models import OrdemServico, StatusOrdemServico
from .forms import OrdermServicoForm
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class OrdemServicoResource(resources.ModelResource):
    class Meta:
        model = OrdemServico
        import_id_fields = ('pedido',)
        fields = ('pedido', 'data_pedido', 'cliente', 'status', 'descricao', 'quantidade')
        widgets = {
            'data_pedido': {'format': '%d/%m/%Y'},
        }


class OrdemServicoAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    resource_class = OrdemServicoResource
    form = OrdermServicoForm
    readonly_fields = ['valor_total', 'situacao']
    list_display = ['numero', 'pedido', 'cliente', 'descricao', 'data_entrega', 'situacao_os']
    search_fields = ['numero', 'pedido', 'cliente__nome', 'cliente__cpf', 'cliente__cnpj',  'descricao', 'data_entrega']
    list_filter = ['status', 'cliente']
    autocomplete_fields = ['cliente']
    fieldsets = (
        ('Identificação', {
            'fields': (
                ('numero', 'pedido', 'status', 'situacao'),
                ('cliente', 'data_pedido', 'data_entrega'),
            )
        }),
        ('Detalhes da O.S.', {
            'fields': (
                ('descricao', 'quantidade'),
                ('valor', 'imposto', 'valor_total'),
                ('observacao',),
            )
        }),
        ('Finalização da O.S.', {
            'fields': (
                ('nota_fiscal', 'data_entrega_real'),
            )
        })
    )

    def situacao_os(self, obj):
        if obj.situacao == 'Entregue com Atraso':
            return format_html(
                '<p style="background-color: yellow;">{0}</p>',
                obj.situacao
            )
        elif obj.situacao == 'Entregue no Prazo':
            return format_html(
                '<p style="background-color: green;">{0}</p>',
                obj.situacao
            )
        elif obj.situacao == 'Pedido Atrasado':
            return format_html(
                '<p style="background-color: tomato;">{0}</p>',
                obj.situacao
            )
        elif obj.situacao == 'Em risco de Atraso':
            return format_html(
                '<p style="background-color: orange;">{0}</p>',
                obj.situacao
            )
        elif obj.situacao == 'Em andamento':
            return format_html(
                '<p style="background-color: cyan;">{0}</p>',
                obj.situacao
            )


admin.site.register(OrdemServico, OrdemServicoAdmin)
admin.site.register(StatusOrdemServico)
