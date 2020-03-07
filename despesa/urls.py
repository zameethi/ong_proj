from django.urls import path
from .views import *

urlpatterns = [
    path('despesa', despesa,  name='despesa'),
    path("lista/", lista_Despesa.as_view()),
    ]
