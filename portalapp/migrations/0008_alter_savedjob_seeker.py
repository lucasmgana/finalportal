# Generated by Django 3.2 on 2021-06-06 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0007_rename_savejob_savedjob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedjob',
            name='seeker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portalapp.profile'),
        ),
    ]
