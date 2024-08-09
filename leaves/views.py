from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Employees, AllocatedLeaves, LeavesTaken
from users.models import Position
from events.models import Events, Announcements
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


@login_required
def leaves(request):
    employee_id = request.user.id  # Change this to the specific employee ID you want to fetch
    employee = Employees.objects.get(id=employee_id)
    allocated_leaves = get_object_or_404(AllocatedLeaves, designation=employee.position)
    employee_name = request.user.name

    if request.method == HTTP_METHOD_POST:
        leave_type = request.POST.get('leave-type')
        start_date = request.POST.get('start-date')
        end_date = request.POST.get('end-date')
        reason = request.POST.get('reason')

        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            leave_days = (end_date - start_date).days + 1

            if leave_type == 'Annual Leave':
                if employee.annual_leaves_taken + leave_days > allocated_leaves.annual_leaves:
                    return JsonResponse({
                        'error': f'You have already taken {employee.annual_leaves_taken} annual leaves. You can take a maximum of {allocated_leaves.annual_leaves - employee.annual_leaves_taken} more annual leaves.'
                    }, status=400)
                employee.annual_leaves_taken += leave_days

            elif leave_type == 'Medical Leave':
                if employee.medical_leaves_taken + leave_days > allocated_leaves.medical_leaves:
                    return JsonResponse({
                        'error': f'You have already taken {employee.medical_leaves_taken} medical leaves. You can take a maximum of {allocated_leaves.medical_leaves - employee.medical_leaves_taken} more medical leaves.'
                    }, status=400)
                employee.medical_leaves_taken += leave_days

            elif leave_type == 'Casual Leave':
                if employee.casual_leaves_taken + leave_days > allocated_leaves.casual_leaves:
                    return JsonResponse({
                        'error': f'You have already taken {employee.casual_leaves_taken} casual leaves. You can take a maximum of {allocated_leaves.casual_leaves - employee.casual_leaves_taken} more casual leaves.'
                    }, status=400)
                employee.casual_leaves_taken += leave_days

            elif leave_type == 'Unpaid Leave':
                employee.unpaid_leaves_taken += leave_days

            employee.save()

            # Add entry to LeavesTaken
            LeavesTaken.objects.create(
                employee_id=employee,
                start_date=start_date,
                end_date=end_date,
                reason=reason,
                leave_type=leave_type,
                leave_taken_count=leave_days
            )

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    context = {
        'employee': employee,
        'allocated_leaves': allocated_leaves,
        'employee_name': employee_name
    }

    return render(request, 'leaves/leaves.html', context)


@login_required
def manage_leaves(request):
    user_role = request.user.role
    permissions = role_permissions.get(user_role, {})
    allocated_leaves = AllocatedLeaves.objects.all()
    employee_name = request.user.name
    pending_leaves = LeavesTaken.objects.filter(status='Pending')

    can_approve = 'approve' in permissions.get('Leaves Approve', [])

    all_designations = Position.objects.all()

    # Get designations already used in AllocatedLeaves
    used_designations = AllocatedLeaves.objects.values_list('designation_id', flat=True)

    # Filter out used designations
    available_designations = all_designations.exclude(id__in=used_designations)

    context = {
        'leaves': allocated_leaves,
        'leaves_permissions': permissions.get('Leaves Count', []),
        'pending_leaves': pending_leaves,
        'can_approve': can_approve,
        'employee_name': employee_name,
        'available_designations': available_designations,
    }

    return render(request, 'leaves/manage_leaves.html', context)


@login_required
@check_permission('Leaves Count', 'create')
def create_leave(request):
    if request.method == HTTP_METHOD_POST:
        designation_id = request.POST.get('designation')
        # print(f"Designation received: {designation_id}")
        annual_leaves = request.POST.get('annual_leaves')
        casual_leaves = request.POST.get('casual_leaves')
        medical_leaves = request.POST.get('medical_leaves')

        try:
            # Get the Position instance based on the designation ID
            designation = Position.objects.get(id=designation_id)
        except Position.DoesNotExist:
            # Handle the error appropriately, e.g., redirect with an error message
            return redirect('manage_leaves')

        # Create the AllocatedLeaves entry
        AllocatedLeaves.objects.create(
            designation=designation,
            annual_leaves=annual_leaves,
            casual_leaves=casual_leaves,
            medical_leaves=medical_leaves
        )
        return redirect('manage_leaves')
    return redirect('manage_leaves')


@login_required
@check_permission('Leaves Count', 'update')
def update_leave(request):
    if request.method == HTTP_METHOD_POST:
        leave_id = request.POST.get('leave_id')
        designation_name = request.POST.get('designation')
        annual_leaves = request.POST.get('annual_leaves')
        casual_leaves = request.POST.get('casual_leaves')
        medical_leaves = request.POST.get('medical_leaves')

        leave = get_object_or_404(AllocatedLeaves, id=leave_id)

        # Get the Position instance based on the designation name
        designation = get_object_or_404(Position, name=designation_name)

        # Update the AllocatedLeaves entry
        leave.designation = designation
        leave.annual_leaves = annual_leaves
        leave.casual_leaves = casual_leaves
        leave.medical_leaves = medical_leaves
        leave.save()
        return redirect('manage_leaves')
    return redirect('manage_leaves')


@login_required
@check_permission('Leaves Count', 'delete')
def delete_leave(request, leave_id):
    leave = get_object_or_404(AllocatedLeaves, id=leave_id)
    leave.delete()
    return redirect('manage_leaves')


@login_required
@check_permission('Leaves Approve', 'approve')
def leave_approve_reject(request, leave_id):
    if 'approve' in role_permissions[request.user.role]['Leaves Approve']:
        leave = get_object_or_404(LeavesTaken, id=leave_id)

        if request.method == HTTP_METHOD_POST:
            action = request.POST.get('action')
            if action == 'approve':
                leave.status = 'Approved'
            elif action == 'reject':
                leave.status = 'Rejected'
            leave.save()
            return redirect('manage_leaves')

    return redirect('manage_leaves')

