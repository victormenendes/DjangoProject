from django.urls import path
from django.contrib import admin
from .views import *
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('produtos/', ProdutosView.as_view(), name='produtos'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('carrinho/', CarrinhoView.as_view(), name='carrinho'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('descricao-produto/', DescricaoProdutoView.as_view(), name='descricao-produto'),
]