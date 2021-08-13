from django.contrib import admin
from portalapp.models import SeekerJobApplication
from .models import Job, Category


class CandidateInline(admin.TabularInline):
    model = SeekerJobApplication

    def get_readonly_fields(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return []
        else:
            return ('candidate',)


class JobAdmin(admin.ModelAdmin):
    exclude = ('creater', 'saved')
    list_display = ('position_name', 'creater',)
    # list_display_links = None
    list_editable = ('creater',)


    def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Job.objects.all()
        else:
            return Job.objects.filter(creater=request.user)

    def get_list_display(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return ('position_name', 'creater','deadline', 'vacancy', 'posted_on', 'saved',)
        else:
            return ('position_name','deadline', 'vacancy', 'posted_on', 'saved',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # assign the creater only on creation and not update
            obj.creater = request.user
            obj.save()

 
admin.site.register(Job, JobAdmin)
admin.site.register(Category)
