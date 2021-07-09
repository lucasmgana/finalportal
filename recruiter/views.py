from portalapp.models import *
from .models import *
from django.views import generic




class IndexView(generic.TemplateView):
    models                      = Job
    template_name               = 'portal/index.html'
    ordering                    = ['available']

    def get_context_data(self, **kwargs):
        context                 = super().get_context_data(**kwargs)
        context['jobs']         = Job.objects.all()
        context["cat_title"]    = Category

        context['page_title'] = self.request
        return context