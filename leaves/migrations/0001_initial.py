# Generated by Django 5.0.7 on 2024-08-07 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllocatedLeaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annual_leaves', models.IntegerField()),
                ('casual_leaves', models.IntegerField()),
                ('medical_leaves', models.IntegerField()),
            ],
            options={
                'db_table': 'AllocatedLeaves',
            },
        ),
        migrations.CreateModel(
            name='LeavesTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.TextField()),
                ('leave_type', models.CharField(max_length=50)),
                ('leave_taken_count', models.IntegerField(default=0)),
                ('status', models.CharField(default='Pending', max_length=20)),
            ],
            options={
                'db_table': 'LeavesTaken',
            },
        ),
    ]
