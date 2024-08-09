from django.http import HttpResponseForbidden
from functools import wraps
from employee_management.const import role_permissions


def check_permission(model_name, permission_type):
    """
    Decorator to check if a user has the required permission for a model.

    :param model_name: Name of the model for which permission is required.
    :param permission_type: Type of permission required (e.g., 'create', 'read', 'update', 'delete').
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user_role = request.user.role
            permissions = role_permissions.get(user_role, {}).get(model_name, [])
            if permission_type not in permissions:
                return HttpResponseForbidden("You do not have permission to perform this action.")
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
