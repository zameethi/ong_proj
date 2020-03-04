from django.urls import path
from .views import *

urlpatterns = [
    path('despesa', despesa,  name='despesa'),
    # path('categoria', categoria,  name='categoria'),

    ]
