from django.urls import path
# from .views import EmployeeDetail, EmployeeList, EventList, AnnouncementList
# from .views import index, profile, login, signup, like_lunch, logout
# from .views import user_list  # user_detail, user_edit, user_delete, user_create
from . import views

urlpatterns = [
    path('', views.manage_projects, name='manage_projects'),
    path('add/', views.add_project, name='add_project'),
    path('edit/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete/<int:project_id>/', views.delete_project, name='delete_project'),
]