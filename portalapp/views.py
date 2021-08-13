from typing import Counter
from django.contrib import messages
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404, redirect, get_list_or_404
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls.base import reverse_lazy, reverse, resolve
from django.views import generic
from jobs.models import Job, Category
from .models import *
from .forms import *
import datetime
from clients.models import Resume

import json  
from datetime import date, datetime
from django.urls import resolve


class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj) 


class IndexView(generic.TemplateView):
    models = Job
    template_name = 'portal/index.html'
    ordering = ['available']

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        context["cat_title"] = Category
        # context['qs_json'] = json.dumps(list(Job.objects.values()), cls=DateEncoder)
        if self.request.user.is_authenticated:
            context['total_saved_jobs'] = SaveJob.objects.filter(seeker=self.request.user).count()

        context['page_title'] = ""
        try:
            context['comp'] = Resume.objects.get(seeker = self.request.user.seeker).completeness
        except:
            context['comp'] = 'Please update resume'
        return context


class SpecificCategory(IndexView):
    template_name = 'portal/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['cat'] = get_object_or_404(Category, title=kwargs['cat'])
            context['jobs'] = get_list_or_404(Job, category=context['cat'])
            context['page_title'] = "Category / " + str(context['cat'])
        except:
            pass
        return context


class CategoryView(IndexView):
    template_name = 'portal/category.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Categories"        
        context['cats'] = Category.objects.all().annotate(
                                    job_s = Count('job')).order_by('-job_s')

        return context


class SingleJob(generic.DetailView):
    template_name = 'portal/singlejob.html'
    model = Job
    context_object_name = 'job'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = str(Job.objects.get(pk=self.kwargs['pk']))
        return context 

@login_required
def SaveJobView(request, pk):
    
    if request.method == 'POST':
        try:
            job = Job.objects.get(pk=pk)
        except:
            save_job = SaveJob.objects.get(pk=pk)
            job = Job.objects.get(pk=save_job.job.pk)

        seeker = request.user
        old = SaveJob.objects.filter(job=job, seeker=seeker).first()
        if old:
            job.saved -= 1
            job.save()
            old.delete()
            messages.info(
                request, "job '{}' is unsaved".format(job.position_name)
            )
            save_status = False
        else:
            job.saved += 1
            job.save()
            SaveJob.objects.create(job=job, seeker = seeker)
            messages.success(
                request, "job '{}' is successfully saved".format(job.position_name)
            )
            save_status = True
    # context = {'saved_status':saved_status}
    return redirect('portalapp:my-saves')


@method_decorator(login_required, name='dispatch')
class ApplicationView(generic.CreateView):
    template_name = 'portal/application.html'
    form_class = SeekerJobApplicationForm
    success_url = reverse_lazy('portalapp:feedback')


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        seeker = request.user
        job = Job.objects.get(pk=self.kwargs['pk'])

        is_already_applied = SeekerJobApplication.objects.filter(job=job, seeker=seeker).first()
        if form.is_valid():
            try:
                is_saved = SaveJob.objects.get(job=job, seeker=request.user)
            except:
                is_saved = None
            if is_saved:
                SaveJobView(request, is_saved.pk)
            form.instance.job = job
            form.instance.seeker = seeker
            form.instance.job_provider = job.creater
            job.vacancy -= 1
            job.save()
            messages.info(
                request, "successfully applied to '" + job.position_name+"'"
            )
            return self.form_valid(form)
        
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Application"

        # job data
        context['total_saved_jobs'] = SaveJob.objects.filter(seeker=self.request.user).count()
        context['applied_job'] = Job.objects.get(pk=self.kwargs['pk'])
        return context
    

@method_decorator(login_required, name='dispatch')
class ProfileView(generic.TemplateView):
    template_name               = 'clients/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_saved_jobs'] = SaveJob.objects.filter(seeker=self.request.user).count()
        context['page_title'] = "Profile"
        return context


@method_decorator(login_required, name='dispatch')
class MyApplicationsView(generic.TemplateView):
    template_name = 'clients/dashboard.html'
    context_object_name = 'applications'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Applications"
        context['total_saved_jobs'] = SaveJob.objects.filter(seeker=self.request.user).count()                
        context['applications'] = SeekerJobApplication.objects.filter(seeker=self.request.user)
        context['total_applied'] = SeekerJobApplication.objects.filter(seeker=self.request.user).count()
        context['accepted'] = SeekerJobApplication.objects.filter(seeker=self.request.user, application_status='accepted').count()
        context['rejected'] = SeekerJobApplication.objects.filter(seeker=self.request.user, application_status='rejected').count()
        context['pending'] = SeekerJobApplication.objects.filter(seeker=self.request.user, application_status='pending').count()
        return context
    

@method_decorator(login_required, name='dispatch')
class FilterView(MyApplicationsView):
    def get_context_data(self, **kwargs):
        context                 = super().get_context_data(**kwargs)
        context['applications'] = SeekerJobApplication.objects.filter(
                                    seeker=self.request.user, application_status=self.kwargs['status']
                                    )
        return context
    

@method_decorator(login_required, name='dispatch')
class MySaveView(generic.TemplateView):
    template_name               = 'clients/saves.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['saved_jobs'] = SaveJob.objects.filter(seeker=self.request.user)
        context['total_saved_jobs'] = SaveJob.objects.filter(seeker=self.request.user).count()
        context['page_title'] = "Saved jobs"
        context['able_to_apply'] = SaveJob.objects.filter(seeker=self.request.user).count()
        return context


class Feedback(MySaveView):
    template_name = 'portal/feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Feedback"
        context["cat_title"] = 'category'
        return context
    