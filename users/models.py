from django.db import models
from employee_management.models import Employees

# Create your models here.


class Feedback(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    feedback = models.TextField()

    class Meta:
        db_table = 'employee_management_feedback'

    def __str__(self):
        return f"{self.employee.name} - Feedback"
