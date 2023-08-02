from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
# Create your views here.


def main_home(request):
    return render(request,'admin/index.html')


def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        if email == "admin@gmail.com" and password == "admin":
            print(email)
            request.session['admin'] = "admin@gmail.com"
            messages.info(request, "Successfully login ")
            return render(request,'admin/admin_home.html')
        elif email != "admin@gmail.com":
            messages.error(request, "Wrong Mail id")
            return render (request,'admin/login.html')
        elif password != "admin":
            messages.error(request,"wrong password")
            return render (request, 'admin/login.html')
        else:
            return render(request,'admin/login.html')
    return render(request,'admin/login.html')


def admin_home(request):
    return render(request,'admin/admin_home.html')


def create_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        task1 = request.POST['task1']
        task2 = request.POST['task2']
        task3 = request.POST['task3']

        if name and email and password and task1 and task2 and task3 is not None:
            try:
                employee(name=name, email=email,password=password,task1=task1,task2=task2,task3=task3).save()
                messages.info(request, "successfully created employee account")
                return redirect('/admin_home/')
            except:
                pass
        else:
             messages.info(request, "Fields Should not be empty")

    return render(request, 'admin/create_employees.html')


def view_employee_details(request):
    data = employee.objects.all()
    return render(request,'admin/employee_details.html',{'data':data})