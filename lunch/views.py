
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import LunchMenu, Admin
from events.models import Events, Announcements
from leaves.models import AllocatedLeaves, LeavesTaken
from django.utils import timezone
from datetime import date, timedelta, datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views import View
from employee_management.const import role_permissions
from django.db import IntegrityError
from django.views.decorators.http import require_POST


import logging

logger = logging.getLogger(__name__)

# Create your views here.


@login_required
def manage_lunch_menu(request):
    user_role = request.user.role
    permissions = role_permissions.get(user_role, {})
    employee_name = request.user.name

    admin = Admin.objects.first()
    all_dishes = LunchMenu.objects.all()

    friday_lunch = all_dishes[:admin.friday_lunch_iterator]
    weekday_lunch = all_dishes[admin.friday_lunch_iterator:admin.friday_lunch_iterator + admin.weekday_lunch_iterator]

    context = {
        'admin': admin,
        'friday_lunch': friday_lunch,
        'weekday_lunch': weekday_lunch,
        'lunch_menu_permissions': permissions.get('Lunch Menu', []),
        'employee_name': employee_name
    }

    return render(request, 'lunch/manage_lunch_menu.html', context)


@login_required
def update_admin(request):
    if request.method == 'POST' and 'update' in role_permissions[request.user.role]['Lunch Menu']:
        admin = Admin.objects.first()
        admin.friday_lunch_iterator = request.POST['friday_lunch_iterator']
        admin.weekday_lunch_iterator = request.POST['weekday_lunch_iterator']
        admin.lunch_time = request.POST['lunch_time']
        admin.save()
    return redirect('manage_lunch_menu')


@login_required
def lunch_menu_create(request):
    if request.method == 'POST' and 'create' in role_permissions[request.user.role]['Lunch Menu']:
        dish_name = request.POST['dish_name']
        LunchMenu.objects.create(dish_name=dish_name)
        return redirect(reverse('manage_lunch_menu'))
    return redirect(reverse('manage_lunch_menu'))


@login_required
def update_lunch_menu(request):
    if request.method == 'POST' and 'update' in role_permissions[request.user.role]['Lunch Menu']:
        dish_id = request.POST['dish_id']
        dish_name = request.POST['dish_name']
        dish = LunchMenu.objects.get(id=dish_id)
        dish.dish_name = dish_name
        dish.save()
    return redirect('manage_lunch_menu')


@login_required
def delete_lunch_menu(request):
    if request.method == 'POST' and 'delete' in role_permissions[request.user.role]['Lunch Menu']:
        dish_id = request.POST['dish_id']
        LunchMenu.objects.filter(id=dish_id).delete()
    return redirect('manage_lunch_menu')
