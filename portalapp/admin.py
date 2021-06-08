from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group



admin.site.register([
    UserRole, Profile, Resume, City, Address, Category, Job,
    Job_wishlist, SavedJob, ApplicationStatus, JobApplication, Comment
    ])
admin.site.unregister(Group)
