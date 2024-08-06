from django.db import models
from employee_management.models import Employees

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=255)
    stack = models.CharField(max_length=255)
    team_members = models.ManyToManyField(Employees)

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.name
