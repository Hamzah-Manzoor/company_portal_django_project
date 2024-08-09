from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Events, Announcements
from django.utils import timezone
from datetime import date, timedelta, datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views import View
from employee_management.const import *
from django.db import IntegrityError
from django.views.decorators.http import require_POST
from employee_management.utils import check_permission


# Create your views here.

@login_required
def events(request):
    upcoming_events = Events.objects.all().order_by('date')
    recent_announcements = Announcements.objects.all().order_by('-date')
    user_permissions = role_permissions[request.user.role]['Events']

    employee_name = request.user.name

    context = {
        'upcoming_events': upcoming_events,
        'recent_announcements': recent_announcements,
        'user_permissions': user_permissions,
        'employee_name': employee_name
    }

    return render(request, 'events/events.html', context)


@login_required
@check_permission('Events', 'create')
def event_create(request):
    if request.method == HTTP_METHOD_POST:
        title = request.POST.get('title')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        Events.objects.create(
            title=title,
            date=date,
            time=time,
            description=description,
            created_by=request.user,
            updated_by=request.user
        )
        return redirect('events')
    return render(request, 'events/event_form.html')


@login_required
@check_permission('Events', 'update')
def event_edit(request, event_id):
    if request.method == HTTP_METHOD_POST:
        event = get_object_or_404(Events, id=event_id)
        title = request.POST.get('title')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        if title and date and time and description:
            event.title = title
            event.date = date
            event.time = time
            event.description = description
            event.updated_by = request.user
            event.save()
            return redirect('events')
        else:
            return render(request, 'events/events.html', {
                'error': 'All fields are required.',
                'upcoming_events': Events.objects.all().order_by('date'),
                'recent_announcements': Announcements.objects.all().order_by('-date')
            })


@login_required
@check_permission('Events', 'delete')
def event_delete(request, event_id):
    if request.method == HTTP_METHOD_POST:
        event = get_object_or_404(Events, id=event_id)
        event.delete()
        return redirect('events')
