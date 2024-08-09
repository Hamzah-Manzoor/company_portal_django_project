from django.db import models
from django.contrib.auth.models import User
from company_portal import settings


class TrackingMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_%(class)s_set', on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_%(class)s_set', on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True