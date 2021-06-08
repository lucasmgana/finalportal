from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.urls.base import reverse_lazy
from django.views import generic
from .models import *
from .forms import *


class IndexView(generic.TemplateView):
    template_name = 'portal/index.html'

    def get_context_data(sel, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'portal/luka mgana'
        context['jobs'] = Job.objects.all()
        return context


class CategoryView(generic.TemplateView):
    template_name = 'portal/category.html'

    def get_context_data(sel, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context


class CatJobs(generic.TemplateView):
    template_name = 'portal/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = get_object_or_404(Category, title=kwargs['cat'])
        context['cats'] = get_list_or_404(Job, category=context['cat'])
        print('all done')
        return context


class SingleJob(generic.DetailView):
    template_name = 'portal/singlejob.html'
    model = Job
    context_object_name = 'job'
    

class Wishlist(generic.TemplateView):
    template_name = 'portal/wishlist.html'
    


class AboutUsView(generic.TemplateView):
    template_name = 'portal/about.html'


class AddCategory(generic.CreateView):
    template_name = 'portal/adddcategory.html'
    form_class = CategoryForm
    success_url = reverse_lazy('portalapp:index')


class ProfileView(generic.TemplateView):
    template_name = 'portal/userprofile.html'


class SaveJob(generic.TemplateView):
    template_name = 'portal/user_profile_bio_graph_and_total_sales.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # grab id from the url request
        job_id = Job.objects.get(id = self.kwargs['pk'])

        # check if the job exist in wishlist
        wishlist_id = self.request.session.get('wishlist_id', None)

        if wishlist_id:
            wishlist_obj = SavedJob.objects.get(id = wishlist_id)
            print('old list')

        else:
            wishlist_obj = SavedJob.objects.create(total = 0)
            self.request.session['wishlist_id'] = wishlist_obj.id
            print('new listed')

        # add job on wishlist
        return context
    