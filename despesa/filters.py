import django_filters
from .models import Despesa

class DespesaFilter(django_filters.FilterSet):

    min_price = django_filters.filters.NumberFilter(field_name="valor_despesa", lookup_expr='gte')
    max_price = django_filters.filters.NumberFilter(field_name="valor_despesa", lookup_expr='lte')
    class Meta:
        model = Despesa
        fields = ['data_despesa', 'valor_despesa', 'max_price', 'min_price']