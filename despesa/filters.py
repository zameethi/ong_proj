import django_filters
from .models import Categoria

class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Categoria
        fields = ['categorias']