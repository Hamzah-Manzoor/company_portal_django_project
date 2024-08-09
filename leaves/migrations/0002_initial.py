# Generated by Django 5.0.7 on 2024-08-07 11:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leaves', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='allocatedleaves',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.position', unique=True),
        ),
        migrations.AddField(
            model_name='leavestaken',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
