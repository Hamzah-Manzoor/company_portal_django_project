from django.db import models

# Create your models here.
from employee_management.models import Employees


class LeavesTaken(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    leave_type = models.CharField(max_length=50)
    leave_taken_count = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='Pending')

    class Meta:
        db_table = 'LeavesTaken'

    def __str__(self):
        return f'{self.employee_id.name} - {self.leave_type} from {self.start_date} to {self.end_date}'


class AllocatedLeaves(models.Model):
    designation = models.CharField(max_length=255)
    annual_leaves = models.IntegerField()
    casual_leaves = models.IntegerField()
    medical_leaves = models.IntegerField()

    class Meta:
        db_table = 'AllocatedLeaves'

    def __str__(self):
        return self.designation

    def update_leaves(self, designation, annual_leaves, casual_leaves, medical_leaves):
        self.designation = designation
        self.annual_leaves = annual_leaves
        self.casual_leaves = casual_leaves
        self.medical_leaves = medical_leaves
        self.save()

    def delete_leaves(self):
        self.delete()

    @classmethod
    def create_leaves(cls, designation, annual_leaves, casual_leaves, medical_leaves):
        leave_record = cls(designation=designation, annual_leaves=annual_leaves, casual_leaves=casual_leaves, medical_leaves=medical_leaves)
        leave_record.save()
        return leave_record
