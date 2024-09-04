
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from users.models import Employees
from events.models import Events, Announcements
from leaves.models import AllocatedLeaves, LeavesTaken
from lunch.models import LunchMenu, Admin, LunchReview
from projects.models import Project
from django.utils import timezone
from datetime import date, timedelta, datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views import View
from .const import *
from .forms import UserCreationForm
from django.db import IntegrityError
from django.views.decorators.http import require_POST


@login_required
def index(request):
    logged_employee = request.user
    employee_name = request.user.name

    # Fetch all employees
    employees = Employees.objects.all()

    # Filter events: the two closest to present time in the future
    upcoming_events = Events.objects.filter(date__gt=timezone.now()).order_by('date')[:2]

    # Filter announcements: the two nearest from the past according to present time
    recent_announcements = Announcements.objects.filter(date__lt=timezone.now()).order_by('-date')[:2]

    # Fetch leaves for the logged employee
    my_employee = Employees.objects.get(id=2)
    allocated_leaves = AllocatedLeaves.objects.get(designation=my_employee.position)
    # allocated_leaves = AllocatedLeaves.objects.get(designation=logged_employee.position)

    # Calculate upcoming birthdays
    today = date.today()
    future_date = today + timedelta(days=10)
    upcoming_birthdays = [
        employee for employee in employees
        if today <= (employee.birthdate.replace(year=today.year) if employee.birthdate.replace(year=today.year) >= today else employee.birthdate.replace(year=today.year + 1))
    ]
    upcoming_birthdays = sorted(upcoming_birthdays, key=lambda x: x.birthdate.replace(year=today.year))[:5]

    # Get the admin details
    admin = Admin.objects.first()

    # Calculate lunch menu
    start_date = datetime.strptime('2024-07-01', '%Y-%m-%d').date()
    days_since_start = (today - start_date).days
    weekdays_since_start = sum(1 for day in range(days_since_start + 1) if (start_date + timedelta(days=day)).weekday() < 5)
    fridays_since_start = sum(1 for day in range(days_since_start + 1) if (start_date + timedelta(days=day)).weekday() == 4)
    weekdays_since_start -= fridays_since_start

    weekday_lunch_iterator = (weekdays_since_start % admin.weekday_lunch_iterator) + admin.friday_lunch_iterator if weekdays_since_start % admin.weekday_lunch_iterator else admin.weekday_lunch_iterator + admin.friday_lunch_iterator
    friday_lunch_iterator = (fridays_since_start % admin.friday_lunch_iterator) if fridays_since_start % admin.friday_lunch_iterator else admin.friday_lunch_iterator

    day_of_week = today.weekday()
    menu_item = "Weekend"
    if day_of_week == 4:
        menu_item = LunchMenu.objects.all()[friday_lunch_iterator - 1]
    elif day_of_week < 4:
        menu_item = LunchMenu.objects.all()[weekday_lunch_iterator - 1]

    lunch_review = None
    if isinstance(menu_item, LunchMenu):
        lunch_review, created = LunchReview.objects.get_or_create(date=today, defaults={'lunch_menu': menu_item})

    # Check if the user has liked or disliked today's lunch
    liked = False
    disliked = False
    if lunch_review:
        liked = logged_employee.id in lunch_review.likes
        disliked = logged_employee.id in lunch_review.dislikes

    # Context to be passed to the template
    context = {
        'employee': logged_employee,
        'employee_name': employee_name,
        'events': upcoming_events,
        'announcements': recent_announcements,
        'upcoming_birthdays': upcoming_birthdays,
        'allocated_leaves': allocated_leaves,
        # For Lunch Card
        'admin': admin,
        'todays_menu': menu_item,
        'likes_count': len(lunch_review.likes) if lunch_review else 0,
        'dislikes_count': len(lunch_review.dislikes) if lunch_review else 0,
        'liked': liked,
        'disliked': disliked,
    }

    return render(request, 'employee_management/index.html', context)


@login_required
def like_lunch(request):
    today = date.today()
    lunch_review = get_object_or_404(LunchReview, date=today)

    user_id = request.user.id

    if request.method == HTTP_METHOD_POST:
        if 'like' in request.POST:
            if user_id in lunch_review.likes:
                lunch_review.likes.remove(user_id)
            else:
                lunch_review.likes.append(user_id)
                if user_id in lunch_review.dislikes:
                    lunch_review.dislikes.remove(user_id)
        elif 'dislike' in request.POST:
            if user_id in lunch_review.dislikes:
                lunch_review.dislikes.remove(user_id)
            else:
                lunch_review.dislikes.append(user_id)
                if user_id in lunch_review.likes:
                    lunch_review.likes.remove(user_id)

        lunch_review.save()

        # Redirect back to the same page
        return redirect(reverse('index'))  # Change 'index' to the name of your index view URL

    return JsonResponse({'error': 'Invalid request method'}, status=400)


# @login_required
# def events(request):
#     upcoming_events = Events.objects.all().order_by('date')
#     recent_announcements = Announcements.objects.all().order_by('-date')
#     user_permissions = role_permissions[request.user.role]['Events']
#
#     employee_name = request.user.name
#
#     context = {
#         'upcoming_events': upcoming_events,
#         'recent_announcements': recent_announcements,
#         'user_permissions': user_permissions,
#         'employee_name': employee_name
#     }
#
#     return render(request, 'employee_management/events.html', context)
#
#
# @login_required
# def event_create(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         description = request.POST.get('description')
#         Events.objects.create(title=title, date=date, time=time, description=description)
#         return redirect('events')
#     return render(request, 'employee_management/event_form.html')
#
#
# @login_required
# def event_edit(request, event_id):
#     if request.method == 'POST':
#         event = get_object_or_404(Events, id=event_id)
#         title = request.POST.get('title')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         description = request.POST.get('description')
#         if title and date and time and description:
#             event.title = title
#             event.date = date
#             event.time = time
#             event.description = description
#             event.save()
#             return redirect('events')
#         else:
#             return render(request, 'events.html', {
#                 'error': 'All fields are required.',
#                 'upcoming_events': Events.objects.all().order_by('date'),
#                 'recent_announcements': Announcements.objects.all().order_by('-date')
#             })
#
#
# @login_required
# def event_delete(request, event_id):
#     if request.method == 'POST':
#         event = get_object_or_404(Events, id=event_id)
#         event.delete()
#         return redirect('events')


# @login_required
# def leaves(request):
#     employee_id = request.user.id  # Change this to the specific employee ID you want to fetch
#     employee = Employees.objects.get(id=employee_id)
#     allocated_leaves = get_object_or_404(AllocatedLeaves, designation=employee.position)
#     employee_name = request.user.name
#
#     if request.method == 'POST':
#         leave_type = request.POST.get('leave-type')
#         start_date = request.POST.get('start-date')
#         end_date = request.POST.get('end-date')
#         reason = request.POST.get('reason')
#
#         try:
#             start_date = datetime.strptime(start_date, '%Y-%m-%d')
#             end_date = datetime.strptime(end_date, '%Y-%m-%d')
#             leave_days = (end_date - start_date).days + 1
#
#             if leave_type == 'Annual Leave':
#                 if employee.annual_leaves_taken + leave_days > allocated_leaves.annual_leaves:
#                     return JsonResponse({
#                         'error': f'You have already taken {employee.annual_leaves_taken} annual leaves. You can take a maximum of {allocated_leaves.annual_leaves - employee.annual_leaves_taken} more annual leaves.'
#                     }, status=400)
#                 employee.annual_leaves_taken += leave_days
#
#             elif leave_type == 'Medical Leave':
#                 if employee.medical_leaves_taken + leave_days > allocated_leaves.medical_leaves:
#                     return JsonResponse({
#                         'error': f'You have already taken {employee.medical_leaves_taken} medical leaves. You can take a maximum of {allocated_leaves.medical_leaves - employee.medical_leaves_taken} more medical leaves.'
#                     }, status=400)
#                 employee.medical_leaves_taken += leave_days
#
#             elif leave_type == 'Casual Leave':
#                 if employee.casual_leaves_taken + leave_days > allocated_leaves.casual_leaves:
#                     return JsonResponse({
#                         'error': f'You have already taken {employee.casual_leaves_taken} casual leaves. You can take a maximum of {allocated_leaves.casual_leaves - employee.casual_leaves_taken} more casual leaves.'
#                     }, status=400)
#                 employee.casual_leaves_taken += leave_days
#
#             elif leave_type == 'Unpaid Leave':
#                 employee.unpaid_leaves_taken += leave_days
#
#             employee.save()
#
#             # Add entry to LeavesTaken
#             LeavesTaken.objects.create(
#                 employee_id=employee,
#                 start_date=start_date,
#                 end_date=end_date,
#                 reason=reason,
#                 leave_type=leave_type,
#                 leave_taken_count=leave_days
#             )
#
#             return JsonResponse({'success': True})
#
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#
#     context = {
#         'employee': employee,
#         'allocated_leaves': allocated_leaves,
#         'employee_name': employee_name
#     }
#
#     return render(request, 'leaves.html', context)
#
#
# @login_required
# def manage_leaves(request):
#     user_role = request.user.role
#     permissions = role_permissions.get(user_role, {})
#     allocated_leaves = AllocatedLeaves.objects.all()
#     employee_name = request.user.name
#     pending_leaves = LeavesTaken.objects.filter(status='Pending')
#
#     can_approve = 'approve' in permissions.get('Leaves Approve', [])
#
#     context = {
#         'leaves': allocated_leaves,
#         'leaves_permissions': permissions.get('Leaves Count', []),
#         'pending_leaves': pending_leaves,
#         'can_approve': can_approve,
#         'employee_name': employee_name
#     }
#
#     return render(request, 'manage_leaves.html', context)
#
#
# @login_required
# def create_leave(request):
#     if request.method == 'POST':
#         designation = request.POST.get('designation')
#         annual_leaves = request.POST.get('annual_leaves')
#         casual_leaves = request.POST.get('casual_leaves')
#         medical_leaves = request.POST.get('medical_leaves')
#
#         AllocatedLeaves.create_leaves(designation, annual_leaves, casual_leaves, medical_leaves)
#         return redirect('manage_leaves')
#     return redirect('manage_leaves')
#
#
# @login_required
# def update_leave(request):
#     if request.method == 'POST':
#         leave_id = request.POST.get('leave_id')
#         designation = request.POST.get('designation')
#         annual_leaves = request.POST.get('annual_leaves')
#         casual_leaves = request.POST.get('casual_leaves')
#         medical_leaves = request.POST.get('medical_leaves')
#
#         leave = get_object_or_404(AllocatedLeaves, id=leave_id)
#         leave.update_leaves(designation, annual_leaves, casual_leaves, medical_leaves)
#         return redirect('manage_leaves')
#     return redirect('manage_leaves')
#
#
# @login_required
# def delete_leave(request, leave_id):
#     leave = get_object_or_404(AllocatedLeaves, id=leave_id)
#     leave.delete_leaves()
#     return redirect('manage_leaves')
#
# @login_required
# def leave_approve_reject(request, leave_id):
#     if 'approve' in role_permissions[request.user.role]['Leaves Approve']:
#         leave = get_object_or_404(LeavesTaken, id=leave_id)
#
#         if request.method == 'POST':
#             action = request.POST.get('action')
#             if action == 'approve':
#                 leave.status = 'Approved'
#             elif action == 'reject':
#                 leave.status = 'Rejected'
#             leave.save()
#             return redirect('manage_leaves')
#
#     return redirect('manage_leaves')


# @login_required
# def profile(request):
#     employee_id = request.user.id  # Replace with the logic to get the current employee's ID
#     employee = get_object_or_404(Employees, id=employee_id)
#     employee_name = request.user.name
#
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         birthdate = request.POST.get('birthdate')
#
#         if name and birthdate:
#             employee.name = name
#             employee.birthdate = birthdate
#             employee.save()
#             return JsonResponse({'success': True})
#         else:
#             return JsonResponse({'success': False, 'error': 'Please fill out all fields.'})
#
#     return render(request, 'profile.html', {'employee': employee, 'employee_name': employee_name})


def signup(request):
    if request.method == HTTP_METHOD_POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == HTTP_METHOD_POST:
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                print("Authentication failed.")
                form.add_error(None, 'Invalid email or password')
        else:
            print("Form is not valid.")
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'employee_management/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')


# @login_required
# def user_list(request):
#     users = Employees.objects.all()
#     user_role = request.user.role
#     employee_name = request.user.name
#
#     user_permissions = role_permissions.get(user_role, {}).get('Users', [])
#
#     context = {
#         'users': users,
#         'user_permissions': user_permissions,
#         'employee_name': employee_name
#     }
#     return render(request, 'employee_management/users.html', context)
#
#
# @login_required()
# def users_create(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         if Employees.objects.filter(email=email).exists():
#             messages.error(request, 'Email already exists')
#             return redirect(reverse('user_list'))
#
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(password)
#             user.save()
#             return redirect(reverse('user_list'))
#
#     return JsonResponse({'error': 'Invalid request method'}, status=400)
#
#
# @login_required
# def user_detail(request, id):
#     user = get_object_or_404(Employees, id=id)
#     return render(request, 'employee_management/user_detail.html', {'user': user})
#
#
# @login_required
# def user_update(request):
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         user = get_object_or_404(Employees, id=user_id)
#         user.name = request.POST.get('name')
#         user.position = request.POST.get('position')
#         user.save()
#         return redirect(reverse('user_list'))
#
#
# @login_required
# def users_delete(request, id):
#     user = get_object_or_404(Employees, id=id)
#     if request.method == 'POST':
#         user.delete()
#         return redirect(reverse('user_list'))
#
#     return JsonResponse({'error': 'Invalid request method'}, status=400)


# @login_required
# def manage_lunch_menu(request):
#     user_role = request.user.role
#     permissions = role_permissions.get(user_role, {})
#     employee_name = request.user.name
#
#     admin = Admin.objects.first()
#     all_dishes = LunchMenu.objects.all()
#
#     friday_lunch = all_dishes[:admin.friday_lunch_iterator]
#     weekday_lunch = all_dishes[admin.friday_lunch_iterator:admin.friday_lunch_iterator + admin.weekday_lunch_iterator]
#
#     context = {
#         'admin': admin,
#         'friday_lunch': friday_lunch,
#         'weekday_lunch': weekday_lunch,
#         'lunch_menu_permissions': permissions.get('Lunch Menu', []),
#         'employee_name': employee_name
#     }
#
#     return render(request, 'manage_lunch_menu.html', context)
#
#
# @login_required
# def update_admin(request):
#     if request.method == 'POST' and 'update' in role_permissions[request.user.role]['Lunch Menu']:
#         admin = Admin.objects.first()
#         admin.friday_lunch_iterator = request.POST['friday_lunch_iterator']
#         admin.weekday_lunch_iterator = request.POST['weekday_lunch_iterator']
#         admin.lunch_time = request.POST['lunch_time']
#         admin.save()
#     return redirect('manage_lunch_menu')
#
#
# @login_required
# def lunch_menu_create(request):
#     if request.method == 'POST' and 'create' in role_permissions[request.user.role]['Lunch Menu']:
#         dish_name = request.POST['dish_name']
#         LunchMenu.objects.create(dish_name=dish_name)
#         return redirect(reverse('manage_lunch_menu'))
#     return redirect(reverse('manage_lunch_menu'))
#
#
# @login_required
# def update_lunch_menu(request):
#     if request.method == 'POST' and 'update' in role_permissions[request.user.role]['Lunch Menu']:
#         dish_id = request.POST['dish_id']
#         dish_name = request.POST['dish_name']
#         dish = LunchMenu.objects.get(id=dish_id)
#         dish.dish_name = dish_name
#         dish.save()
#     return redirect('manage_lunch_menu')
#
#
# @login_required
# def delete_lunch_menu(request):
#     if request.method == 'POST' and 'delete' in role_permissions[request.user.role]['Lunch Menu']:
#         dish_id = request.POST['dish_id']
#         LunchMenu.objects.filter(id=dish_id).delete()
#     return redirect('manage_lunch_menu')


# @login_required
# def manage_projects(request):
#     user_role = request.user.role
#     project_permissions = role_permissions.get(user_role, {}).get('Projects', [])
#     employee_name = request.user.name
#
#     can_create = 'create' in project_permissions
#     can_update = 'update' in project_permissions
#     can_delete = 'delete' in project_permissions
#
#     # Retrieve all projects and employees
#     projects = Project.objects.all()
#     employees = Employees.objects.all()
#
#     context = {
#         'projects': projects,
#         'employees': employees,
#         'can_create': can_create,
#         'can_update': can_update,
#         'can_delete': can_delete,
#         'employee_name': employee_name,
#     }
#
#     return render(request, 'projects.html', context)
#
#
# @login_required
# def add_project(request):
#     user_role = request.user.role
#     if 'create' not in role_permissions.get(user_role, {}).get('Projects', []):
#         return redirect('manage_projects')
#
#     if request.method == 'POST':
#         project_name = request.POST.get('project_name')
#         stack = request.POST.get('stack')
#         team_members = request.POST.getlist('team_members')
#
#         # Create the new project
#         project = Project.objects.create(name=project_name, stack=stack)
#
#         if team_members:
#             # Ensure that only non-empty IDs are used
#             team_members = [member_id for member_id in team_members if member_id]
#
#         if team_members:
#             project.team_members.set(team_members)
#
#         project.save()
#
#     return redirect('manage_projects')
#
#
# @login_required
# def edit_project(request, project_id):
#     user_role = request.user.role
#     if 'update' not in role_permissions.get(user_role, {}).get('Projects', []):
#         return redirect('manage_projects')
#
#     project = get_object_or_404(Project, id=project_id)
#
#     if request.method == 'POST':
#         project.name = request.POST.get('project_name')
#         project.stack = request.POST.get('stack')
#         team_members = request.POST.getlist('team_members')
#
#         project.team_members.set(team_members)
#         project.save()
#
#     return redirect('manage_projects')
#
#
# @login_required
# def delete_project(request, project_id):
#     user_role = request.user.role
#     if 'delete' not in role_permissions.get(user_role, {}).get('Projects', []):
#         return redirect('manage_projects')
#
#     project = get_object_or_404(Project, id=project_id)
#     project.delete()
#     return redirect('manage_projects')


# @login_required
# def manage_feedback(request):
#     user = request.user
#     role = user.role
#     permissions = role_permissions.get(role, {}).get('Feedback', [])
#     employee_name = request.user.name
#
#     if role in ['S-HR', 'J-HR']:
#         feedbacks = Feedback.objects.all()
#     else:
#         feedbacks = Feedback.objects.filter(employee=user)
#
#     context = {
#         'feedbacks': feedbacks,
#         'user': user,
#         'employee_name': employee_name,
#         'perms': {
#             'feedback': {
#                 'create': 'create' in permissions,
#                 'read': 'read' in permissions,
#                 'update': 'update' in permissions,
#                 'delete': 'delete' in permissions,
#             }
#         }
#     }
#
#     return render(request, 'feedback.html', context)
#
#
# @login_required
# def add_feedback(request):
#     print("-----------------------------------------")
#     print("You are in add feedback")
#     print("-----------------------------------------")
#     if request.method == 'POST':
#         employee_id = request.POST.get("employee_id")
#         feedback_text = request.POST.get('feedback')
#
#         try:
#             Feedback.objects.create(employee_id=employee_id, feedback=feedback_text)
#             return redirect('manage_feedback')
#         except IntegrityError as e:
#             print(f"IntegrityError: {e}")
#
#             user = request.user
#             role = user.role
#             permissions = role_permissions.get(role, {}).get('Feedback', [])
#             employee_name = request.user.name
#
#             if role in ['S-HR', 'J-HR']:
#                 feedbacks = Feedback.objects.all()
#             else:
#                 feedbacks = Feedback.objects.filter(employee=user)
#
#             context = {
#                 'feedbacks': feedbacks,
#                 'user': user,
#                 'employee_name': employee_name,
#                 'error_message': 'Failed to add feedback. Please ensure the Employee ID is valid.',
#                 'perms': {
#                     'feedback': {
#                         'create': 'create' in permissions,
#                         'read': 'read' in permissions,
#                         'update': 'update' in permissions,
#                         'delete': 'delete' in permissions,
#                     }
#                 }
#             }
#
#             return render(request, 'feedback.html', context)
#
#     return redirect('manage_feedback')
#
#
# @login_required
# def edit_feedback(request, feedback_id):
#     feedback = get_object_or_404(Feedback, id=feedback_id)
#     if request.method == 'POST':
#         feedback.feedback = request.POST.get('feedback')
#         feedback.save()
#         return redirect('manage_feedback')
#     return redirect('manage_feedback')
#
#
# @login_required
# def delete_feedback(request, feedback_id):
#     feedback = get_object_or_404(Feedback, id=feedback_id)
#     if request.method == 'POST':
#         feedback.delete()
#         return redirect('manage_feedback')
#     return redirect('manage_feedback')
