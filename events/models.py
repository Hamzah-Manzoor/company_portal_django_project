from django.db import models
from employee_management.mixins import TrackingMixin

# Create your models here.


class Events(TrackingMixin, models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'Events'

    def __str__(self):
        return self.title


class Announcements(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    details = models.TextField()

    class Meta:
        db_table = 'Announcements'

    def __str__(self):
        return self.title
