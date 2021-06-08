# Generated by Django 3.2 on 2021-06-06 14:42

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
            name='ApplicationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccancy', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('company', models.CharField(max_length=255)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('dadeline', models.DateField()),
                ('available', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portalapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to='media')),
                ('first_name', models.CharField(default='', max_length=255, verbose_name='Full Name')),
                ('gender', models.CharField(default='', max_length=255, verbose_name='Gender')),
                ('date_of_birth', models.DateField()),
                ('phone', models.CharField(max_length=244)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='profile owner')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portalapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('certificates', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('user_profile', models.CharField(max_length=50)),
                ('seeker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portalapp.profile', verbose_name='Seeker')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portalapp.userrole', verbose_name='user role'),
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apply_at', models.DateTimeField()),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portalapp.job', verbose_name='Job applied')),
                ('seeker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='seeker')),
                ('status', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portalapp.applicationstatus', verbose_name='application status')),
            ],
        ),
        migrations.CreateModel(
            name='Job_wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portalapp.job', verbose_name='Job')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('wishlist', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portalapp.wishlist')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='commentor')),
                ('job_commented', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portalapp.job', verbose_name='Job commented')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_code', models.CharField(max_length=50)),
                ('address_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Client | company')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portalapp.city', verbose_name='Region')),
            ],
        ),
    ]
