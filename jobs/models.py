from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime

class Category(models.Model):
    category_id = models.AutoField(primary_key = True)
    title  = models.CharField(max_length=255)


    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('index')
    
    @property
    def get_jobs_by_category(self):
        cat_jobs = self.jobs_set.all()
        return cat_jobs

    @property
    def get_total_jobs_by_category(self):
        cat_jobs = self.jobs_set.all().Count()
        return cat_jobs

experience_choice = [
    ('', 'choose job experience'),
    ('0 - 1 (yrs)', '0 - 1 (yrs)'),
    ('1 - 2 (yrs)', '1 - 2 (yrs)'),
    ('1 - 3 (yrs)', '1 - 3 (yrs)'),
    ('2 - 3 (yrs)', '2 - 3 (yrs)'),
    ('Above 3 (yrs)', 'Above 3 (yrs)'),
]


class Job(models.Model):
    job_id = models.AutoField(primary_key = True)
    position_name = models.CharField(max_length = 100)
    descriptions = models.TextField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    salary = models.IntegerField()
    vacancy = models.PositiveIntegerField(default = 1)
    creater = models.ForeignKey(User, on_delete = models.CASCADE)
    experience = models.CharField(_('Experience (yrs)'), choices=experience_choice, max_length = 244, blank = True, null = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    deadline = models.DateField()
    posted_on = models.DateField(auto_now_add=True)
    saved = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position_name

    def get_absolute_url(self):    
        return reverse('index')


    def clean(self):
        if self.deadline <= datetime.now().date():
            raise ValidationError('Deadline should be greater than Posted time')


        if self.max_age <= self.min_age:
            raise ValidationError('Min age should be less than or equal to max age')
