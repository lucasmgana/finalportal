from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *


class SeekerJobApplicationForm(forms.ModelForm):
    # full_name = forms.CharField(widget=forms.TextInput(attrs={'required':'required'}))
    job_title = forms.CharField(widget=forms.TextInput(attrs={'required':'required'}))
    # job_status = forms.CharField(widget=forms.TextInput(attrs={'required':'required'}))
    seeker_email = forms.EmailField(widget=forms.EmailInput(attrs={'required':'required'}))
    seeker_phone = forms.CharField(widget=forms.TextInput(attrs={'required':'required'}))
    # seeker_job_experience = forms.CharField(widget=forms.TextInput(attrs={'required':'required'}))
    seeker_cv = forms.FileField(widget=forms.FileInput(attrs={'required':'required'}))

    class Meta:
        model = SeekerJobApplication

        fields = (
            "full_name", "job_title", "job_status", "seeker_email",
            "seeker_phone", "seeker_job_experience", "seeker_cv"
            )

    def __init__(self, *args, **kwargs):
        super(SeekerJobApplicationForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].widget.attrs['readonly'] = True
        self.fields['full_name'].widget.attrs['readonly'] = True
        self.fields['seeker_job_experience'].widget.attrs['class'] = 'form-control'



class SaveJobForm(forms.ModelForm):
    class Meta:
        model = SaveJob
        fields = "__all__"