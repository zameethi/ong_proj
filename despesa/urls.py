from django.urls import path
from .views import *

urlpatterns = [
    path('despesa', despesa,  name='despesa'),
    path('despesa/<int:pk>', editar_despesas,  name='atualiza'),
    path("lista/", lista_Despesa.as_view()),
    ]
