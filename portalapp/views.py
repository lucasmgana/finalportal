from django.shortcuts import render
from django.views import generic
from .models import *


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(sel, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'luka mgana'
        context['jobs'] = Job.objects.all()
        return context

class CategoryView(generic.TemplateView):
    template_name = 'category.html'

    def get_context_data(sel, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'luka mgana'
        context['cats'] = Category.objects.all()
        return context




class AboutUsView(generic.TemplateView):
    template_name = 'about.html'


class ContactUsView(generic.TemplateView):
    template_name = 'contactus.html'