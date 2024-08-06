from django.urls import path
# from .views import EmployeeDetail, EmployeeList, EventList, AnnouncementList
from .views import profile
# from .views import user_list  # user_detail, user_edit, user_delete, user_create
from . import views


urlpatterns = [
    path('profile/', profile, name='profile'),

    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.users_create, name='users_create'),
    path('users/delete/<int:id>/', views.users_delete, name='users_delete'),
    path('users/update/', views.user_update, name='user_update'),

    path('feedback/', views.manage_feedback, name='manage_feedback'),
    path('feedback/add/', views.add_feedback, name='add_feedback'),
    path('feedback/edit/<int:feedback_id>/', views.edit_feedback, name='edit_feedback'),
    path('feedback/delete/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
]