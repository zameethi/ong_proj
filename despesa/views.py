import datetime
import inspect
import sys
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
from django_tables2 import SingleTableView, LazyPaginator, RequestConfig, SingleTableMixin
from .filters import *
from .tables import TabelaDespesa
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
sys.path.append("..")


@login_required
def despesa(request):
    self = inspect.currentframe().f_code.co_name
    hoje = datetime.datetime.today().strftime('%Y-%m-%d')

    print(hoje)
    # Lista de Despesas
    lista_despesas = Despesa.objects.all()

    # formulario para Documentos
    form_documentos = documentos_form()

    # formulario para Trasasações
    form_transacao = transacao_form()

    print(lista_despesas.values())

    # Parametros para Despesa
    doc = TipoDocumento.objects.all()
    trans = TipoTransacao.objects.all()
    val = request.GET.dict()

    q = request.GET.get('categorias')
    if q != '':
        categorias = Categoria.objects.filter(id=q)
    else:
        categorias = Categoria.objects.filter(id=0)
    if request.method=='GET':
        q = request.GET.get('categorias')
        if q != '':
            categorias = Categoria.objects.filter(id=q)
        despesas = despesa_form(request.GET or None, initial=val)
        return render(request, 'geral/despesas.html', {'self':self, 'despesa': despesas, 'categoria': categorias, 'documento': doc, 'transacao': trans, 'lista': lista_despesas, 'hoje':hoje})
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

    return render(request, 'geral/despesas.html', {'self':self ,'despesa': despesas, 'categoria': categorias, 'documento': doc, 'transacao': trans, 'lista': lista_despesas, 'hoje':hoje})

class lista_Despesa(SingleTableMixin, FilterView):
    table_class = TabelaDespesa
    model = Despesa
    template_name = "geral/lista.html"
    filterset_class = DespesaFilter


def editar_despesas(request, pk):
    self = inspect.currentframe().f_code.co_name
    lista_desp = Despesa.objects.get(pk=pk)
    despesas = despesa_form(request.POST or None, instance=lista_desp)

    # formulario para Documentos
    form_documentos = documentos_form()

    # formulario para Trasasações
    form_transacao = transacao_form()

    val = request.GET.dict()
    categorias = Categoria.objects.filter(descricao_categoria=lista_desp.categorias, subcategorias=lista_desp.subcategorias)
    lista_despesas = Despesa.objects.all()
    doc = TipoDocumento.objects.all()
    trans = TipoTransacao.objects.all()
    print(categorias.values('subcategorias'))

    if request.method == 'GET':
        if len(val) == 0:
            pass
        else:
            q = request.GET.get('categorias')
            if q != '':
                categorias = Categoria.objects.filter(id=q)
                print(categorias)
                despesas = despesa_form(request.GET or None, initial=val)
    if request.method == 'POST' or None:
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
    return render(request, 'geral/edit-despesas.html',
                  {'self':self,'despesa': despesas, 'categoria': categorias, 'documento': doc, 'transacao': trans,
                   'lista': lista_despesas})
