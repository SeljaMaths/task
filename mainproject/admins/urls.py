from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.main_home, name='main_home'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('view_employee_details/', views.view_employee_details, name='view_employee_details')

    ]