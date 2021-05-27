from django.shortcuts import get_object_or_404, render, get_list_or_404
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
        context['cats'] = Category.objects.all()
        return context


class CatJobs(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = get_object_or_404(Category, title=kwargs['cat'])
        context['cats'] = get_list_or_404(Job, category=context['cat'])
        print('all done')
        return context



class SingleJob(generic.DetailView):
    template_name = 'singlejob.html'
    model = Job
    context_object_name = 'job'
    

class Wishlist(generic.TemplateView):
    template_name = 'wishlist.html'
    


class AboutUsView(generic.TemplateView):
    template_name = 'about.html'


class ContactUsView(generic.TemplateView):
    template_name = 'contactus.html'