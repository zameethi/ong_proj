from django import forms
from .models import *



class despesa_form(forms.ModelForm):
    estado = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id': 'estado', 'value': ' '}))
    valor_despesa = forms.CharField(max_length=10)
    conciliado = forms.ChoiceField(choices=(
                                    (0, "Não"),
                                    (1, "Sim")
                                ), initial=0)

    class Meta:
        model = Despesa
        fields = '__all__'

    def clean_valor_despesa(self):
        data = self.cleaned_data['valor_despesa']
        data = round(float(data.replace('.','').replace(',','.')),2)
        return data

    # def __init__(self, categorias, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['categorias'].queryset = Categoria.objects.filter(id=categorias)

class documentos_form(forms.ModelForm):

    class Meta:
        model = TipoDocumento
        fields = '__all__'


class transacao_form(forms.ModelForm):

    class Meta:
        model = TipoTransacao
        fields = '__all__'


