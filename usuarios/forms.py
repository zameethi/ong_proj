from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render

# Create your views here.

# class CustomUserCreationForm(forms.Form):
class UserRegisterForm(forms.Form):
    username = forms.CharField(label='Entre com Usuário', min_length=4, max_length=150)
    email = forms.EmailField(label='Entre com o Email')
    password1 = forms.CharField(label='Entre com a Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)

    class Meta:
        labels = {'username': 'Usuário',
                  'password1': 'Senha',
                  'password2': 'Senha',
                  }

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Usuário existente")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email existente")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Senha não é igual")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user