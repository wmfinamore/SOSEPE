from django import forms
from .models import OrdemServico


class OrdermServicoForm(forms.ModelForm):
    data_pedido = forms.DateField(widget=forms.widgets.TextInput(attrs={'type': 'date'}), required=False)
    data_entrega = forms.DateField(widget=forms.widgets.TextInput(attrs={'type': 'date'}), required=False)
    data_entrega_real = forms.DateField(widget=forms.widgets.TextInput(attrs={'type': 'date'}), required=False)

