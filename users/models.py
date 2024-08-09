from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from lunch.models import LunchMenu

# Create your models here.


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'Position'

    def __str__(self):
        return self.name


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
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True)
    date_of_joining = models.DateField(blank=True, null=True)
    birthdate = models.DateField(blank=False, null=False, default='1990-05-15')
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


class Feedback(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    feedback = models.TextField()

    class Meta:
        db_table = 'Feedback'

    def __str__(self):
        return f"{self.employee.name} - Feedback"




