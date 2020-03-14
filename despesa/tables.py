import django_tables2 as tables
from django_tables2 import A

from .models import Despesa

class TabelaDespesa(tables.Table):

    class Meta:
        model = Despesa
        template_name = "django_tables2/bootstrap4.html"
        fields = ('data_despesa','valor_despesa', "descricao_despesa", "documento", "transacao", "conciliado", "categorias", "subcategorias")
        attrs = {'th': {'class': 'table-primary'}}

        orderable = True

