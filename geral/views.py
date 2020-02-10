from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
@login_required
def home(request):
    now = datetime.datetime.now()
    html = "<html><body> Agora é %s</body></html>" %now
    return render(request,'geral/dashboard.html')

def view_excel(request):
    return render(request,'geral/teste.html')

