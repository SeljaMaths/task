from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import logout
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
    data = employee.objects.filter(assign_task=False)
    return render(request,'admin/employee_details.html',{'data':data})


def send_mail_employee_details(request,pk):
    data = employee.objects.get(pk=pk)
    msg = f"Hello, My name is {data.name} and your email id and password {data.email}. and" \
          f"{data.password}. we are assigning your task can you check your email id."
    send_mail(
        'Assigning task',
        msg,
        "authentication4email@gmail.com",
        [data.email],
        fail_silently=False,
    )
    data.assign_task = True
    data.save()
    messages.info(request, "Email sent to employee")

    return redirect("/admin_home/")


def employee_report(request):
    data = employee.objects.filter(employee_report=True)
    return render(request,'admin/update_employee_details.html',{'data':data})


def update_employee_details(request,pk):
    x = employee.objects.get(pk=pk)
    if request.method == "POST":
        x.name = request.POST.get('name')
        x.email= request.POST.get('email')
        x.task1 = request.POST.get('task1')
        x.task2 = request.POST.get('task2')
        x.task3 = request.POST.get('task3')
        x.save()
        return redirect('/admin_home/')
    messages.info(request, "Successfully updates")
    return render(request, 'admin/update.html', {'x': x})


def delete_employee(request,pk):
    x = employee.objects.get(pk=pk)
    x.delete()
    messages.info(request, "Deleted")
    return redirect('/admin_home/')


def admin_logout(request):
    logout(request)
    return redirect('/')


