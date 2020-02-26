from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
#from .forms import CustomUserCreationForm
from .forms import UserRegisterForm

# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         f = CustomUserCreationForm(request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('register')
#     else:
#         f = CustomUserCreationForm()
#
#     return render(request, 'cadmin/register.html', {'form': f})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Sua conta foi criado com sucesso!')
            form.save()
            return redirect('login')
        else:
            messages.error(request, f'Não foi possivel criar!')
    else:
        form = UserRegisterForm()
    return render(request, 'cadmin/register.html', {'form': form})


@login_required
def profile(request):
    print(request.POST, request.GET)
    return render(request, 'cadmin/profile.html')