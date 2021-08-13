from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Seeker, Resume
from portalapp.models import SeekerJobApplication
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_field = [
        'date_joinded', 'email',
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs) 
        form.base_fields['username'].disabled = True
        
        return form


class ApplicationResource(resources.ModelResource):
    class Meta:
        model = SeekerJobApplication


class SeekerAdmin(ImportExportModelAdmin):
    list_display = (
                    'seeker', 'job', 'full_name', 'seeker_email','job_provider', 
                    'application_status','seeker_job_experience',
                    )

    list_filter = ('application_status', 'seeker_job_experience',)
    resource_class = ApplicationResource


class ReviewSeekerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'age', 'gender', 'expected_salary', 'profile_image', 'date_of_birth', 'phone')
    list_filter = ('age','gender', 'expected_salary', )
    list_editable = []
    # list_display_links = None


admin.site.register(Seeker, ReviewSeekerAdmin)
admin.site.register(Resume)

admin.site.site_header = 'Job Portal'
admin.site.site_title = 'Job Portal'
admin.site.index_title = 'Job Portal'
admin.site.site_url = 'Job Portal'