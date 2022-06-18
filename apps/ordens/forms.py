from django import forms
from .models import OrdemServico


class OrdemServicoForm(forms.ModelForm):
    data_pedido = forms.DateField(widget=forms.widgets.TextInput(attrs={'type': 'date'}), required=False)
    data_entrega = forms.DateField(widget=forms.widgets.TextInput(attrs={'type': 'date'}), required=False)
    data_entrega_real = forms.DateField(widget=forms.widgets.TextInput(attrs={'type': 'date'}), required=False)

    def __init__(self, *args, **kwargs):
        super(OrdemServicoForm, self).__init__(*args, **kwargs)

        if self.instance.id:
            if self.instance.situacao == 'Entregue com Atraso':
                self.fields["numero"].widget.attrs["style"] = 'background-color: yellow;'
            elif self.instance.situacao == 'Entregue no Prazo':
                self.fields["numero"].widget.attrs["style"] = 'background-color: green;'
            elif self.instance.situacao == 'Pedido Atrasado':
                self.fields["numero"].widget.attrs["style"] = 'background-color: tomato;'
            elif self.instance.situacao == 'Em risco de Atraso':
                self.fields["numero"].widget.attrs["style"] = 'background-color: orange;'
            elif self.instance.situacao == 'Em andamento':
                self.fields["numero"].widget.attrs["style"] = 'background-color: cyan;'

        class Meta:
            model: OrdemServico
