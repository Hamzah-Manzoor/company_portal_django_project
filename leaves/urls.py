from django.urls import path
# from .views import EmployeeDetail, EmployeeList, EventList, AnnouncementList
from .views import leaves
# from .views import user_list  # user_detail, user_edit, user_delete, user_create
from . import views

urlpatterns = [
    path('', views.manage_leaves, name='manage_leaves'),
    path('create/', views.create_leave, name='leave_create'),
    path('update/', views.update_leave, name='leave_update'),
    path('delete/<int:leave_id>/', views.delete_leave, name='leave_delete'),
    path('leave_approve_reject/<int:leave_id>/', views.leave_approve_reject, name='leave_approve_reject'),
    path('apply_leaves/', views.leaves, name='apply_leaves'),
]