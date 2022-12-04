from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.


class IndexView(TemplateView):
    template_name = 'Store/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class ProdutosView(TemplateView):
    template_name = 'Store/produtos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Produtos'
        return context

class ContatoView(TemplateView):
    template_name = 'Store/contato.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contato'
        return context

class CarrinhoView(TemplateView):
    template_name = 'Store/carrinho.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Carrinho'
        return context

class WishlistView(TemplateView):
    template_name = 'Store/wishlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wishlist'
        return context

class DescricaoProdutoView(TemplateView):
    template_name = 'Store/descricao-produto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Descricao-produto'
        return context