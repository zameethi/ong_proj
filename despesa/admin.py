from django import forms
from django.contrib import admin
from .models import *
from .forms import *

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['subcategorias']
    search_fields = ['subcategorias']

@admin.register(Subcategoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['subcategorias']



@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['subcategorias']
    search_fields = ['subcategorias']


admin.site.register(TipoDocumento)
admin.site.register(TipoTransacao)
# admin.site.register(Despesa)







