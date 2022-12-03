from django.urls import path
from django.contrib import admin
from .views import *
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('produtos/', ProdutosView.as_view(), name='produtos'),
]