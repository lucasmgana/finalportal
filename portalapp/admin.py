from django.contrib import admin
from .models import *



admin.site.register([UserRole, User, Profile, Resume, City, Address, Category, Job, Job_wishlist, ApplicationStatus, JobApplication, Comment])

