from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from lunch.models import LunchMenu


class EmployeesManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class Employees(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    date_of_joining = models.DateField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    annual_leaves_taken = models.IntegerField(default=0)
    casual_leaves_taken = models.IntegerField(default=0)
    medical_leaves_taken = models.IntegerField(default=0)
    unpaid_leaves_taken = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    role = models.CharField(max_length=255, choices=[
        ('CEO', 'CEO'),
        ('CTO', 'CTO'),
        ('S-HR', 'Senior HR'),
        ('J-HR', 'Junior HR'),
        ('Project Manager', 'Project Manager'),
        ('Team Lead', 'Team Lead'),
        ('Employee', 'Employee')
    ], default='Employee')

    objects = EmployeesManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'Employees'

    def __str__(self):
        return self.email


# class LeavesTaken(models.Model):
#     employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     reason = models.TextField()
#     leave_type = models.CharField(max_length=50)
#     leave_taken_count = models.IntegerField(default=0)
#     status = models.CharField(max_length=20, default='Pending')
#
#     class Meta:
#         db_table = 'LeavesTaken'
#
#     def __str__(self):
#         return f'{self.employee_id.name} - {self.leave_type} from {self.start_date} to {self.end_date}'


# class Events(models.Model):
#     title = models.CharField(max_length=255)
#     date = models.DateField()
#     time = models.CharField(max_length=50)
#     description = models.TextField()
#
#     class Meta:
#         db_table = 'Events'
#
#     def __str__(self):
#         return self.title


# class Announcements(models.Model):
#     title = models.CharField(max_length=255)
#     date = models.DateField()
#     details = models.TextField()
#
#     class Meta:
#         db_table = 'Announcements'
#
#     def __str__(self):
#         return self.title


# class LunchMenu(models.Model):
#     dish_name = models.CharField(max_length=255)
#
#     class Meta:
#         db_table = 'LunchMenu'
#
#     def __str__(self):
#         return self.dish_name


# class AllocatedLeaves(models.Model):
#     designation = models.CharField(max_length=255)
#     annual_leaves = models.IntegerField()
#     casual_leaves = models.IntegerField()
#     medical_leaves = models.IntegerField()
#
#     class Meta:
#         db_table = 'AllocatedLeaves'
#
#     def __str__(self):
#         return self.designation
#
#     def update_leaves(self, designation, annual_leaves, casual_leaves, medical_leaves):
#         self.designation = designation
#         self.annual_leaves = annual_leaves
#         self.casual_leaves = casual_leaves
#         self.medical_leaves = medical_leaves
#         self.save()
#
#     def delete_leaves(self):
#         self.delete()
#
#     @classmethod
#     def create_leaves(cls, designation, annual_leaves, casual_leaves, medical_leaves):
#         leave_record = cls(designation=designation, annual_leaves=annual_leaves, casual_leaves=casual_leaves, medical_leaves=medical_leaves)
#         leave_record.save()
#         return leave_record


# class Admin(models.Model):
#     friday_lunch_iterator = models.IntegerField()
#     weekday_lunch_iterator = models.IntegerField()
#     lunch_time = models.TimeField(default="15:00:00")  # Assuming default lunch time
#
#     class Meta:
#         db_table = 'admin'
#
#     def __str__(self):
#         return f'FridayIterator: {self.friday_lunch_iterator}, WeekdayIterator: {self.weekday_lunch_iterator}, LunchTime: {self.lunch_time}'


class LunchReview(models.Model):
    date = models.DateField(default=timezone.now)
    lunch_menu = models.ForeignKey(LunchMenu, on_delete=models.CASCADE)
    likes = models.JSONField(default=list, blank=True)
    dislikes = models.JSONField(default=list, blank=True)

    class Meta:
        db_table = 'lunch_review'

    def __str__(self):
        return f'Date: {self.date}, Menu: {self.lunch_menu}, Likes: {len(self.likes)}, Dislikes: {len(self.dislikes)}'


# class Project(models.Model):
#     name = models.CharField(max_length=255)
#     stack = models.CharField(max_length=255)
#     team_members = models.ManyToManyField('Employees')
#
#     class Meta:
#         db_table = 'projects'
#
#     def __str__(self):
#         return self.name


# class Feedback(models.Model):
#     employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
#     feedback = models.TextField()
#
#     def __str__(self):
#         return f"{self.employee.name} - Feedback"

