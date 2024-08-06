
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Project
from employee_management.models import Employees
from events.models import Events, Announcements
from leaves.models import AllocatedLeaves, LeavesTaken
from lunch.models import LunchMenu, Admin
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
def manage_projects(request):
    user_role = request.user.role
    project_permissions = role_permissions.get(user_role, {}).get('Projects', [])
    employee_name = request.user.name

    can_create = 'create' in project_permissions
    can_update = 'update' in project_permissions
    can_delete = 'delete' in project_permissions

    # Retrieve all projects and employees
    projects = Project.objects.all()
    employees = Employees.objects.all()

    context = {
        'projects': projects,
        'employees': employees,
        'can_create': can_create,
        'can_update': can_update,
        'can_delete': can_delete,
        'employee_name': employee_name,
    }

    return render(request, 'projects/projects.html', context)


@login_required
def add_project(request):
    user_role = request.user.role
    if 'create' not in role_permissions.get(user_role, {}).get('Projects', []):
        return redirect('manage_projects')

    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        stack = request.POST.get('stack')
        team_members = request.POST.getlist('team_members')

        # Create the new project
        project = Project.objects.create(name=project_name, stack=stack)

        if team_members:
            # Ensure that only non-empty IDs are used
            team_members = [member_id for member_id in team_members if member_id]

        if team_members:
            project.team_members.set(team_members)

        project.save()

    return redirect('manage_projects')


@login_required
def edit_project(request, project_id):
    user_role = request.user.role
    if 'update' not in role_permissions.get(user_role, {}).get('Projects', []):
        return redirect('manage_projects')

    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        project.name = request.POST.get('project_name')
        project.stack = request.POST.get('stack')
        team_members = request.POST.getlist('team_members')

        project.team_members.set(team_members)
        project.save()

    return redirect('manage_projects')


@login_required
def delete_project(request, project_id):
    user_role = request.user.role
    if 'delete' not in role_permissions.get(user_role, {}).get('Projects', []):
        return redirect('manage_projects')

    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('manage_projects')