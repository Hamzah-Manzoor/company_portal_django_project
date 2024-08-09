from django.urls import path
# from .views import EmployeeDetail, EmployeeList, EventList, AnnouncementList
from .views import index, login, signup, like_lunch, logout
# from .views import user_list  # user_detail, user_edit, user_delete, user_create
from . import views

# app_name = 'employee_management'

urlpatterns = [
    path('', index, name='index'),

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('like_lunch/', like_lunch, name='like_lunch'),

]
