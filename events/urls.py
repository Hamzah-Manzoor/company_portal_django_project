from django.urls import path
# from .views import EmployeeDetail, EmployeeList, EventList, AnnouncementList
from .views import events
# from .views import user_list  # user_detail, user_edit, user_delete, user_create
from . import views

urlpatterns = [
    path('', events, name='events'),
    path('create/', views.event_create, name='event_create'),
    path('edit/<int:event_id>/', views.event_edit, name='event_edit'),
    path('delete/<int:event_id>/', views.event_delete, name='event_delete'),
]