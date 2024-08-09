from django.contrib import admin

# Register your models here.
from django.contrib import admin

from users.models import *
from projects.models import *
from lunch.models import *
from leaves.models import *
from events.models import *

# admin.site.register(Employees)
admin.site.register(Position)
# admin.site.register(Employees)

admin.site.register(Project)

admin.site.register(LunchMenu)
admin.site.register(Admin)
admin.site.register(LunchReview)

admin.site.register(LeavesTaken)
admin.site.register(AllocatedLeaves)

admin.site.register(Events)
admin.site.register(Announcements)

admin.site.register(Feedback)







from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Employees


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
