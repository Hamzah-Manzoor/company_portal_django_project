# Generated by Django 5.0.7 on 2024-08-07 11:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='team_members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
