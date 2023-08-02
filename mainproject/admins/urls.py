from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.main_home, name='main_home'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('view_employee_details/', views.view_employee_details, name='view_employee_details'),
    path('send_mail_employee_details/<int:pk>/', views.send_mail_employee_details, name='send_mail_employee_details'),
    path('update_employee_details/<int:pk>/', views.update_employee_details, name='update_employee_details'),
    path('delete_employee/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('admin_logout/', views.admin_logout,name='admin_logout'),
    path('employee_report/', views.employee_report, name='employee_report'),


    ]