from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


from django.utils import timezone
from datetime import datetime, date

# user data related
# ////////////////////////////////////////////////////////////////////////////////////////
class UserRole(models.Model):
    rolename            = models.CharField(max_length=50)

    def __str__(self):
        return self.rolename



class Profile(models.Model):
    role                = models.ForeignKey(UserRole, verbose_name= "user role", on_delete=models.CASCADE)
    client              = models.OneToOneField(User, verbose_name= "profile owner", on_delete=models.CASCADE)
    profile_image       = models.ImageField(upload_to='media', max_length=None)
    full_name           = models.CharField(verbose_name='Full Name', default="", blank= False, null= False, name="first_name", max_length=255)
    gender              = models.CharField(verbose_name='Gender', default="", blank= False, null= False, name="gender", max_length=255)
    date_of_birth       = models.DateField()
    phone               = models.CharField(max_length = 244)

    def __str__(self):
        return str(self.client)
    


class Resume(models.Model):
    seeker              = models.OneToOneField(Profile, verbose_name= "Seeker", on_delete=models.CASCADE)
    cv_attachment                  =  models.CharField(max_length=50)
    education_level           =  models.CharField(max_length=50)
    certificates        =  models.CharField(max_length=50)
    hire_status              =  models.CharField(max_length=50)

    def __str__(self):
        return str(self.seeker) + " the seeker"



class City(models.Model):
    name                = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


class Address(models.Model):
    address_user        = models.ForeignKey(User, verbose_name= "Client | company", on_delete=models.CASCADE)
    post_code           = models.CharField(max_length=50)
    city                = models.ForeignKey(City, verbose_name= "Region", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.address_user) + ", " + self.post_code + ", " + str(self.city)


    class Meta:
        verbose_name_plural = 'Address'



# JOB RELATED DATA
# //////////////////////////////////////////////////////////////////////////////

class Category(models.Model):
    title               = models.CharField(max_length=255)


    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('index')
    
    
    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)

    


        
class Job(models.Model):
    category            = models.ForeignKey(Category, on_delete=models.CASCADE)
    vaccancy            = models.CharField(max_length=255)
    description         = models.CharField(max_length=500)
    company             = models.CharField(max_length=255)
    posted_on           = models.DateTimeField(auto_now_add=True)
    dadeline            = models.DateField()
    available           = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.vaccancy
    
    def get_absolute_url(self):    
        # should return url to redirect to recreiter site
        return reverse('index')



# PROCESSING TABLES
# //////////////////////////////////////////////////////////////////////////////////
class SavedJob(models.Model):
    seeker              = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False, null=True)
    total               = models.PositiveIntegerField()
    created_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "wishlist " + str(self.id)

class Job_wishlist(models.Model):
    wishlist            = models.ForeignKey(SavedJob,  on_delete=models.CASCADE, default=1)
    user_email          = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    job_id              = models.ForeignKey(Job, verbose_name="Job", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_email) + " wishes " + str(self.job_id)


class ApplicationStatus(models.Model):
    status_name         = models.CharField(max_length=50)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name_plural = 'ApplicationStatuses'
    


class JobApplication(models.Model):
    seeker              = models.OneToOneField(User, verbose_name= "seeker", on_delete=models.CASCADE)
    job                 = models.OneToOneField(Job, verbose_name= "Job applied", on_delete=models.CASCADE)
    status              = models.OneToOneField(ApplicationStatus, verbose_name= "application status", on_delete=models.CASCADE)
    Apply_at            = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.seeker) + " applied to " + str(self.job)


class Comment(models.Model):
    commentor           = models.ForeignKey(User, verbose_name="commentor", on_delete=models.CASCADE)
    job_commented       = models.OneToOneField(Job, verbose_name="Job commented", on_delete=models.CASCADE)
    comment           = models.TextField()

    def __str__(self):
        return " commented on:" + str(self.job_commented)



