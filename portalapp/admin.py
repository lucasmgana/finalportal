from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import *
from django.contrib.auth.models import Group


class SeekerJobApplicationResource(resources.ModelResource):
    class Meta:
        model = SeekerJobApplication


class SeekerApplicationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
                    'seeker', 'job', 'full_name', 'seeker_email','job_provider', 
                    'application_status',
                    )
    list_filter = ('job','job_provider', 
                    'application_status',
                    )
    list_per_page = 20
    list_editable = ('application_status',)

    resource_class = SeekerJobApplicationResource
    list_display_links = None


    def get_queryset(self, request, *args, **kwargs):
        return SeekerJobApplication.objects.filter(job_provider=request.user.username)

    def get_list_display(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return ('seeker_email','full_name', 'job_title', 'job_provider', 'application_status','seeker_job_experience',)
        else:
            return ('full_name', 'seeker_email', 'job_title', 'application_status','seeker_job_experience',)

admin.site.register(SeekerJobApplication, SeekerApplicationAdmin)
admin.site.register(SaveJob)
