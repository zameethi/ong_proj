import sys

from django_filters.views import FilterView
from django_tables2 import SingleTableView, LazyPaginator, RequestConfig, SingleTableMixin
from .filters import *
from .tables import TabelaDespesa
sys.path.append("..")
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def despesa(request):
    # Lista de Despesas
    lista_despesas = Despesa.objects.all()

    # formulario para Documentos
    form_documentos = documentos_form()

    # formulario para Trasasações
    form_transacao = transacao_form()

    # Parametros para Despesa
    doc = TipoDocumento.objects.all()
    trans = TipoTransacao.objects.all()
    val = request.GET.dict()
    print(val)
    q = request.GET.get('categorias')
    if q != '':
        categorias = Categoria.objects.filter(id=q)
    else:
        categorias = Categoria.objects.filter(id=0)
    despesas = despesa_form(initial=val)
    if request.method=='GET':
        q = request.GET.get('categorias')
        if q != '':
            categorias = Categoria.objects.filter(id=q)
        despesas = despesa_form(request.GET or None, initial=val)
        return render(request, 'geral/despesas.html', {'despesa': despesas, 'categoria': categorias, 'documento': doc, 'transacao': trans, 'lista': lista_despesas})
    if request.method=='POST':
        despesas = despesa_form(request.POST or None)
        form_documentos = documentos_form(request.POST or None)
        form_transacao = transacao_form(request.POST or None)
        if request.method=='POST' or None:
            if despesas.is_valid():
                despesas.save()
                messages.success(request, 'Despesa salva.')
                return redirect('despesa')
            elif form_documentos.is_valid():
                form_documentos.save()
                messages.success(request, 'Tipo de documento Salvo.')
                val = request.POST.dict()
            elif form_transacao.is_valid():
                form_transacao.save()
                messages.success(request, 'Tipo de transação Salvo.')
                val = request.POST.dict()
    despesas = despesa_form(request.GET or request.POST or None, initial=val)

    return render(request, 'geral/despesas.html', {'despesa': despesas, 'categoria': categorias, 'documento': doc, 'transacao': trans, 'lista': lista_despesas})

class lista_Despesa(SingleTableMixin, FilterView):
    table_class = TabelaDespesa
    model = Despesa
    template_name = "geral/lista_bootstrap4.html"

    filterset_class = DespesaFilter

# def lista_Despesa(request):
#     queryset = Despesa.objects.all()
#     table = TabelaDespesa(queryset)
#     table.paginate(page=request.GET.get("page", 1), per_page=10)
#     RequestConfig(request).configure(table)
#     return render(request, 'geral/lista.html', {'table': table})