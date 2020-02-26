from django import forms
from django.contrib import admin
from .models import *

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['subcategoria']


@admin.register(Subcategoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['descricao_subcategoria']



admin.site.register(TipoDocumento)
admin.site.register(TipoTransacao)
admin.site.register(Despesa)



