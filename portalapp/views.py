from typing import Counter

from django.db.models.aggregates import Count
from jobapplication.models import Order
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.urls.base import reverse_lazy, reverse, resolve
from django.views import generic
from .models import *
from .forms import *
from .customerfunctions import *
import json

import json  
from datetime import date, datetime
from django.urls import resolve

# from urllib.parse import urlparse
# from django.http import Http404, HttpResponseRedirect
# def page_url(request):
#     next = request.META.get('HTTP_REFERER', None) or '/'
#     match = resolve(next)
#     return match.url_name

class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj) 




class IndexView(generic.TemplateView):
    models                      = Job
    template_name               = 'portal/landingpage.html'
    ordering                    = ['available']

    def get_context_data(self, **kwargs):
        context                 = super().get_context_data(**kwargs)
        context['jobs']         = Job.objects.all()
        context["cat_title"]    = Category
        context['qs_json']      = json.dumps(list(Job.objects.values()), cls=DateEncoder)

        context['page_title']   = ""
        return context


class CategoryView(generic.TemplateView):
    template_name               = 'portal/category.html'


    def get_context_data(self, **kwargs):
        context                 = super().get_context_data(**kwargs)
        context['page_title']   = "Categories"
        
        context['cats']         = Category.objects.all().annotate(
            job_s = Count('job')).order_by('-job_s')

        return context



class SpecificCategory(generic.TemplateView):
    template_name = 'portal/index.html'

    def get_context_data(self, **kwargs):
        context                     = super().get_context_data(**kwargs)
        try:
            context['cat']          = get_object_or_404(Category, title=kwargs['cat'])
            context['jobs']         = get_list_or_404(Job, category=context['cat'])
            context['page_title']   = "Category / " + str(context['cat'])

        except:
            pass
        return context


class SingleJob(generic.DetailView):
    template_name               = 'portal/singlejob.html'
    model                       = Job
    context_object_name         = 'job'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title']   = str(Job.objects.get(id=self.kwargs['pk']))
        return context
    
    



class SaveJob(generic.TemplateView):
    template_name = 'clients/profile.html'


    def get_context_data(self, **kwargs):
        context                 = super().get_context_data(**kwargs)

        # grab id from the url request
        job_id                  = Job.objects.get(id = self.kwargs['pk'])

        # check if the job exist in wishlist
        wishlist_id             = self.request.session.get('wishlist_id', None)

        if wishlist_id:
            wishlist_obj        = SavedJob.objects.get(id = wishlist_id)
            print('old list')

        else:
            wishlist_obj        = SavedJob.objects.create(total = 0)
            self.request.session['wishlist_id'] = wishlist_obj.id
            print('new listed')

        # add job on wishlist
        return context



class ApplicationView(generic.TemplateView):
    template_name               = 'portal/application.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        next = self.request.GET.get('next')
        context['page_title']   = "Application"
        print(next)
        return context
    





class Wishlist(generic.TemplateView):
    template_name               = 'portal/wishlist.html'
    


class Feedback(generic.TemplateView):
    template_name               = 'portal/feedback.html'

    def get_context_data(self, **kwargs):
        context                 = super().get_context_data(**kwargs)
        context['page_title']   = "Feedback"
        context["cat_title"]    = 'category'
        return context
    


class ProfileView(generic.TemplateView):
    template_name               = 'clients/profile.html'

    def get_context_data(self, **kwargs):
        context                 = super().get_context_data(**kwargs)
        context['page_title']   = "Profile"
        context["profile"]      = Profile.objects.get(client=self.kwargs['pk'])
        return context
    
