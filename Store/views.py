from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.


class IndexView(TemplateView):
    template_name = 'Store/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context