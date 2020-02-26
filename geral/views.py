from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
@login_required
def home(request):
    data = ["55","30","5", "10"]
    labels = ["Valor 1", "Valor 2", "Valor 3", "Valor 4"]
    return render(request,'geral/dashboard.html', {'data': str(data).replace("'",'"'), 'label': str(labels).replace("'",'"')})

def view_excel(request):
    return render(request,'geral/teste.html')

