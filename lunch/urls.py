from django.urls import path
# from .views import EmployeeDetail, EmployeeList, EventList, AnnouncementList
# from .views import index, profile, login, signup, like_lunch, logout
# from .views import user_list  # user_detail, user_edit, user_delete, user_create
from . import views

urlpatterns = [
    path('', views.manage_lunch_menu, name='manage_lunch_menu'),
    path('update_admin/', views.update_admin, name='admin_update'),
    path('create/', views.lunch_menu_create, name='lunch_menu_create'),
    path('update/', views.update_lunch_menu, name='lunch_menu_update'),
    path('delete/', views.delete_lunch_menu, name='lunch_menu_delete'),
]