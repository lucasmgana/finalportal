# Generated by Django 3.2.5 on 2021-08-01 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=244)),
            ],
        ),
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('seeker_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=20)),
                ('expected_salary', models.IntegerField(blank=True, null=True)),
                ('will_relocate', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=244, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('resume_id', models.AutoField(primary_key=True, serialize=False)),
                ('olevel_certificate', models.CharField(max_length=50)),
                ('advance_level_certificate', models.CharField(max_length=50)),
                ('collage_level_certificate', models.CharField(max_length=50)),
                ('high_level_certificate', models.CharField(max_length=50)),
                ('seeker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clients.seeker', verbose_name='Seeker')),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('recruiter_id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_image', models.ImageField(upload_to='media')),
                ('first_name', models.CharField(default='', max_length=255, verbose_name='Full Name')),
                ('gender', models.CharField(default='', max_length=255, verbose_name='Gender')),
                ('date_of_birth', models.DateField(blank=True)),
                ('phone', models.CharField(max_length=244)),
                ('company', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='clients.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='profile owner')),
            ],
        ),
    ]
