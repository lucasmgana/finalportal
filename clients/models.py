from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime


# user data related
# ////////////////////////////////////////////////////////////////////////////////////////

GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_CHOICES = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
)

STATUS_PENDING = 'pending'
STATUS_ACCEPTED = 'accepted'
STATUS_REJECTED = 'rejected'
STATUS_CHOICES = (
    (STATUS_PENDING, 'Pending'),
    (STATUS_ACCEPTED, 'Accepted'),
    (STATUS_REJECTED, 'Rejected'),
)





class Seeker(models.Model):
    seeker_id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, default=GENDER_MALE)
    expected_salary = models.IntegerField(null=True, blank=True)

    profile_image       = models.ImageField(upload_to='media', max_length=None, null=True, blank=True)
    date_of_birth       = models.DateField(null=True, blank=True)
    phone  = models.CharField(max_length = 244, null=True, blank=True)
    

    def __str__(self):
        return str(self.user)


    # def save(self, **kwargs):
    #     dob = self.date_of_birth
    #     dot = datetime.date().today()
    #     yrs = relativedelta(dot, dob)
    #     diff = yrs.years
    #     return super().save(self, **kwargs)


class Resume(models.Model):
    resume_id = models.AutoField(primary_key=True)
    seeker              =  models.OneToOneField('Seeker', verbose_name= "Seeker", on_delete=models.CASCADE)
    olevel_certificate       =  models.FileField(upload_to = 'olevel')
    advance_level_certificate     =  models.FileField(upload_to = 'advance')
    collage_level_certificate        =  models.FileField(upload_to = 'collage')
    high_level_certificate        =  models.FileField(upload_to = 'high level')

    def __str__(self):
        return str(self.seeker) + " the seeker"

    @property
    def completeness(self):
        if self.olevel_certificate and self.advance_level_certificate and self.high_level_certificate or self.collage_level_certificate:
            return '100%'

        elif self.olevel_certificate and self.advance_level_certificate and self.high_level_certificate:
            return '90%'

        elif self.olevel_certificate and self.advance_level_certificate and self.collage_level_certificate:
            return '75%'

        elif self.olevel_certificate and self.advance_level_certificate:
            return '50%'
        
        elif self.olevel_certificate:
            return '10%'
        
        else:
            return '0%'




class Recruiter(models.Model):
    recruiter_id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, verbose_name= "profile owner", on_delete=models.CASCADE)
    profile_image       = models.ImageField(upload_to='media', max_length=None)
    full_name           = models.CharField(verbose_name='Full Name', default="", blank= False, null= False, name="first_name", max_length=255)
    gender = models.CharField(verbose_name='Gender', default="", blank= False, null= False, name="gender", max_length=255)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, blank= True, null= False, max_length=255)
    date_of_birth       = models.DateField(blank= True, null= False,)
    phone  = models.CharField(max_length = 244)


    def __str__(self):
        return str(self.user)


    def clean(self):
        if date_of_birth >= datetime.datetime.now().date() and date_of_birth >= datetime.timedelta(years - 18):
            raise ValidationError('enter valid birth date')
    

class Company(models.Model):
    company_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=244, blank = True, null=False)

    def __str__(self):
        return self.name
    

