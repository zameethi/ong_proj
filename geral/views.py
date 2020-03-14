import itertools
import sys
import calendar
import datetime
from django.db.models import Sum, Count, Avg
from django.db.models.functions import TruncMonth
import operator as op
sys.path.append("..")
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from despesa.models import *
import datetime

# Create your views here.
@login_required
def home(request):
    dados = Despesa.objects.all().values('valor_despesa', 'categorias').order_by('data_despesa')
    data = []
    labels = []
    for item in dados:
        # print(item['categorias'])
        data.append(f"{item['valor_despesa']}")
        data1 = Categoria.objects.filter(id=item['categorias'])[0]
        labels.append(str(data1)[:10])
        # print(data1)

    dados_soma = []
    labels_soma = []

    for cat in Despesa.objects.all().values('categorias').distinct():
        ids = (cat['categorias'])
        a = (Categoria.objects.filter(id=cat['categorias'])[0])
        dteste1 = Despesa.objects.filter(categorias=ids).aggregate(Sum('valor_despesa'))['valor_despesa__sum']
        dados_soma.append(str(dteste1))
        labels_soma.append(str(a).replace(',',';')[:10])

    soma = (Despesa.objects.aggregate(Sum('valor_despesa'))['valor_despesa__sum'])

    media = round(Despesa.objects.all().aggregate(Avg('valor_despesa'))['valor_despesa__avg'],2)

    agora = datetime.datetime.now()

    porcento = round(((agora.day)/(calendar.monthrange(agora.year, agora.month)[1]))*100)

    qs = Despesa.objects.values('data_despesa').values('data_despesa')
    grouped = itertools.groupby(qs, lambda d: d.get('data_despesa').strftime('%Y-%m-%d'))

    mes = Despesa.objects.annotate(month=TruncMonth('data_despesa')).values('month').annotate(numeros=Count('id')).order_by()


    return render(request,'geral/dashboard.html', {'data': str(data).replace("'",'"'), 'label': str(labels).replace("'",'"'),
                                                   'data2': str(dados_soma).replace("'",'"'), 'label2': str(labels_soma).replace("'",'"'),
                                                   'soma':soma, 'media': media, 'porcento': porcento})

def view_excel(request):
    return render(request,'geral/teste.html')

