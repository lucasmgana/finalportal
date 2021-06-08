from django import forms
from django.db.models import fields
from .models import *


class JobApplicationForm(forms.ModelForm):
    
    class Meta:
        fields = "__all__"
        model = JobApplication
        


class CategoryForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Category