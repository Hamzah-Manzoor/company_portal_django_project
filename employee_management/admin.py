from django.contrib import admin

# Register your models here.
from django.contrib import admin
from leaves.models import AllocatedLeaves

admin.site.register(AllocatedLeaves)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employees


class EmployeeAdmin(UserAdmin):
    model = Employees
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'birthdate', 'date_of_joining', 'position')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Employees, EmployeeAdmin)
