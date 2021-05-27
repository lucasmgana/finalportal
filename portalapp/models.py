from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, date
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# user data related
# ////////////////////////////////////////////////////////////////////////////////////////
class UserRole(models.Model):
    rolename = models.CharField(max_length=50)

    def __str__(self):
        return self.rolename



class UserManager(BaseUserManager):
    def create_user(
                    self, first_name, 
                    surname, gender, resumes, company, 
                    profile, email, password=None, middle_name = None
                                ):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_applicant(self, first_name, surname, gender, 
                             email, resumes = None, 
                            password=None, middle_name = None, profile = None):
        user = self.create_user(
                            first_name, surname, gender, 
                            email, resumes = None, password=None, middle_name = None, profile = None
                             )


    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# hook in the New Manager to our Model
# class User(AbstractBaseUser): # from step 2
    # ...
    # objects = UserManager()


class User(AbstractBaseUser):
    role = models.OneToOneField(UserRole, verbose_name= "user role", on_delete=models.CASCADE)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'surname', 'gender'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + " " + self.surname

    def get_short_name(self):
        # The user is identified by their email address
        return self.surname

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is user an admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


class Profile(models.Model):
    user        = models.OneToOneField(User, verbose_name= "profile owner", on_delete=models.CASCADE)
    full_name  = models.CharField(verbose_name='Full Name', default="", blank= False, null= False, name="first_name", max_length=255)
    gender      = models.CharField(verbose_name='Gender', default="", blank= False, null= False, name="gender", max_length=255)
    date_of_birth = models.DateField()
    phone  = models.CharField(max_length = 244)

    def __str__(self):
        return self.user + " " + self.full_name
    


class Resume(models.Model):
    seeker = models.OneToOneField(Profile, verbose_name= "Seeker", on_delete=models.CASCADE)
    cv =  models.CharField(max_length=50)
    education =  models.CharField(max_length=50)
    certificates =  models.CharField(max_length=50)
    status =  models.CharField(max_length=50)
    user_profile =  models.CharField(max_length=50)

    def __str__(self):
        return self.seeker + " the seeker"



class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Address(models.Model):
    address_user  = models.ForeignKey(User, verbose_name= "Client | company", on_delete=models.CASCADE)
    post_code = models.CharField(max_length=50)
    city = models.ForeignKey(City, verbose_name= "Region", on_delete=models.CASCADE)

    def __str__(self):
        return self.address_user + ", " + self.postal_code + ", " + self.city





# JOB RELATED DATA
# //////////////////////////////////////////////////////////////////////////////

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('index')

        
class Job(models.Model):
    vaccancy = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    company = models.CharField(max_length=255)
    posted_on = models.DateTimeField(auto_now_add=True)
    dadeline = models.DateField()
    available = models.PositiveIntegerField(default = 0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.vaccancy
    
    def get_absolute_url(self):        
        return reverse('index')



# PROCESSING TABLES
# //////////////////////////////////////////////////////////////////////////////////

class Job_wishlist(models.Model):
    user_email = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, verbose_name="Job", on_delete=models.CASCADE)

    def __str__(self):
        return self.user_email + " wishes " + self.job_id


class ApplicationStatus(models.Model):
    status_name = models.CharField(max_length=50)

    def __str__(self):
        return self.status_name


class JobApplication(models.Model):
    seeker = models.OneToOneField(User, verbose_name= "seeker", on_delete=models.CASCADE)
    job = models.OneToOneField(Job, verbose_name= "Job applied", on_delete=models.CASCADE)
    status = models.OneToOneField(ApplicationStatus, verbose_name= "application status", on_delete=models.CASCADE)
    Apply_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.user + " applied to " + self.job


class Comment(models.Model):
    commentor = models.ForeignKey(User, verbose_name="commentor", on_delete=models.CASCADE)
    job_commented = models.OneToOneField(Job, verbose_name="Job commented", on_delete=models.CASCADE)

    def __str__(self):
        return self.commentor + " comments, " + self.job_commented