# Generated by Django 3.2.5 on 2021-08-01 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20210801_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='advance_level_certificate',
            field=models.FileField(upload_to='advance'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='collage_level_certificate',
            field=models.FileField(upload_to='collage'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='high_level_certificate',
            field=models.FileField(upload_to='high level'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='olevel_certificate',
            field=models.FileField(upload_to='olevel'),
        ),
    ]