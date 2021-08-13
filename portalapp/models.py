from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django.utils import timezone
from datetime import datetime, date


application_status =[
    ('pending','pending'),
    ('accepted','accepted'),
    ('rejected','rejected'),
]


class SeekerJobApplication(models.Model):
    seeker_application_id = models.AutoField(primary_key = True)
    job = models.ForeignKey('jobs.Job', on_delete = models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_status = models.CharField(max_length=255)
    seeker = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length = 255)
    seeker_email = models.EmailField(max_length =255)
    seeker_phone = models.CharField(max_length = 255)
    job_provider = models.CharField(max_length = 255)
    application_date = models.DateTimeField(auto_now_add=True)
    seeker_job_experience = models.CharField(max_length = 255)
    application_status = models.CharField(choices=application_status, default=application_status[0][0], max_length = 255)
    seeker_cv = models.FileField(upload_to = 'cvs')


    def __str__(self):
        return "{} - {}".format(self.full_name, self.job.position_name)

    class Meta:
        verbose_name_plural = "Review Applications"


class SaveJob(models.Model):
    savejob_id = models.AutoField(primary_key = True)
    seeker = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} is saved by {}'.format(str(self.job), str(self.seeker))
