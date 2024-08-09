
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Employees, Feedback, Position
from events.models import Events, Announcements
from leaves.models import AllocatedLeaves, LeavesTaken
from lunch.models import LunchMenu, Admin
from projects.models import Project
from django.utils import timezone
from datetime import date, timedelta, datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views import View
from employee_management.const import *
from employee_management.forms import UserCreationForm
from django.db import IntegrityError
from django.views.decorators.http import require_POST
from functools import wraps
from employee_management.utils import check_permission


@login_required
def profile(request):
    employee_id = request.user.id  # Replace with the logic to get the current employee's ID
    employee = get_object_or_404(Employees, id=employee_id)
    employee_name = request.user.name

    if request.method == HTTP_METHOD_POST:
        name = request.POST.get('name')
        birthdate = request.POST.get('birthdate')

        if name and birthdate:
            employee.name = name
            employee.birthdate = birthdate
            employee.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Please fill out all fields.'})

    return render(request, 'users/profile.html', {'employee': employee, 'employee_name': employee_name})


@login_required
def user_list(request):
    users = Employees.objects.all()
    user_role = request.user.role
    employee_name = request.user.name

    user_permissions = role_permissions.get(user_role, {}).get('Users', [])

    positions = Position.objects.all()

    context = {
        'users': users,
        'user_permissions': user_permissions,
        'employee_name': employee_name,
        'positions': positions,
    }
    return render(request, 'users/users.html', context)


# def check_permission(permission):
#     def decorator(view_func):
#         @wraps(view_func)
#         def _wrapped_view(request, *args, **kwargs):
#             user_role = request.user.role
#             user_permissions = role_permissions.get(user_role, {}).get('Users', [])
#             if permission in user_permissions:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 messages.error(request, 'You do not have permission to perform this action.')
#                 return redirect(reverse('user_list'))
#         return _wrapped_view
#     return decorator


@login_required()
@check_permission('Users', 'create')
def users_create(request):
    if request.method == HTTP_METHOD_POST:
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Employees.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect(reverse('user_list'))

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return redirect(reverse('user_list'))

    return JsonResponse({'error': 'Invalid request method'}, status=400)


@login_required
def user_detail(request, id):
    user = get_object_or_404(Employees, id=id)
    return render(request, 'users/user_detail.html', {'user': user})


@login_required
@check_permission('Users', 'update')
def user_update(request):
    if request.method == HTTP_METHOD_POST:
        user_id = request.POST.get('user_id')
        user = get_object_or_404(Employees, id=user_id)
        user.name = request.POST.get('name')

        position_id = request.POST.get('position')
        position = get_object_or_404(Position, id=position_id)
        user.position = position

        user.save()
        return redirect(reverse('user_list'))


@login_required
@check_permission('Users', 'delete')
def users_delete(request, id):
    user = get_object_or_404(Employees, id=id)
    if request.method == HTTP_METHOD_POST:
        user.delete()
        return redirect(reverse('user_list'))

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def get_permissions(role, category):
    return role_permissions.get(role, {}).get(category, [])


def get_permission_dict(role, category):
    permissions = get_permissions(role, category)
    return {
        'create': 'create' in permissions,
        'read': 'read' in permissions,
        'update': 'update' in permissions,
        'delete': 'delete' in permissions,
    }


# def check_feedback_permission(permission):
#     def decorator(view_func):
#         @wraps(view_func)
#         def _wrapped_view(request, *args, **kwargs):
#             user_role = request.user.role
#             permissions = get_permissions(user_role, 'Feedback')
#             if permission in permissions:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 messages.error(request, 'You do not have permission to perform this action.')
#                 return redirect(reverse('manage_feedback'))
#         return _wrapped_view
#     return decorator


@login_required
def manage_feedback(request):
    user = request.user
    role = user.role
    permissions = role_permissions.get(role, {}).get('Feedback', [])
    employee_name = request.user.name

    if role in ['S-HR', 'J-HR']:
        feedbacks = Feedback.objects.all()
    else:
        feedbacks = Feedback.objects.filter(employee=user)

    context = {
        'feedbacks': feedbacks,
        'user': user,
        'employee_name': employee_name,
        'perms': {
            'feedback': get_permission_dict(role, 'Feedback')
        }
    }

    return render(request, 'users/feedback.html', context)


@login_required
@check_permission('Feedback', 'create')
def add_feedback(request):
    if request.method == HTTP_METHOD_POST:
        employee_id = request.POST.get("employee_id")
        feedback_text = request.POST.get('feedback')

        try:
            Feedback.objects.create(employee_id=employee_id, feedback=feedback_text)
            return redirect('manage_feedback')
        except IntegrityError as e:
            print(f"IntegrityError: {e}")

            user = request.user
            role = user.role
            permissions = role_permissions.get(role, {}).get('Feedback', [])
            employee_name = request.user.name

            if role in ['S-HR', 'J-HR']:
                feedbacks = Feedback.objects.all()
            else:
                feedbacks = Feedback.objects.filter(employee=user)

            context = {
                'feedbacks': feedbacks,
                'user': user,
                'employee_name': employee_name,
                'error_message': 'Failed to add feedback. Please ensure the Employee ID is valid.',
                'perms': {
                    'feedback': get_permission_dict(role, 'Feedback')
                }
            }

            return render(request, 'users/feedback.html', context)

    return redirect('manage_feedback')


@login_required
@check_permission('Feedback', 'update')
def edit_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    if request.method == HTTP_METHOD_POST:
        feedback.feedback = request.POST.get('feedback')
        feedback.save()
        return redirect('manage_feedback')
    return redirect('manage_feedback')


@login_required
@check_permission('Feedback', 'delete')
def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    if request.method == HTTP_METHOD_POST:
        feedback.delete()
        return redirect('manage_feedback')
    return redirect('manage_feedback')
