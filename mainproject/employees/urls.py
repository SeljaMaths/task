from django.urls import path,include
from . import views

urlpatterns = [
    path('employee_home/', views.employee_home, name='employee_home'),
    path('employee_login/', views.employee_login,name='employee_login'),
    path('view_task/', views.view_task, name='view_task'),
    path('update_register/<int:pk>/', views.update_register,name='update_register'),
    path('employee_logout/', views.employee_logout, name='employee_logout')
]