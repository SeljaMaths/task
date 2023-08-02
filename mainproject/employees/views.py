from django.shortcuts import render,redirect
from .models import *
from admins.models import *
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


def employee_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = employee.objects.get(email=email, password=password, assign_task=True)
            request.session['employee'] = r.email

            if r is not None:
                messages.info(request, 'welcome')
                return redirect('/employee_home/')
        except:
            pass

    else:
        return render(request, 'employee/login.html')


def employee_home(request):
    return render(request,'employee/employee_home.html')


def view_task(request):
    obj = employee.objects.filter(email=request.session['employee'], assign_task=True)
    return render(request,'employee/view_task.html',{'obj':obj})


def update_register(request,pk):
    update = employee.objects.get(pk=pk)
    if request.method == "POST":
        update.task1= request.POST.get('task1')
        update.task2=request.POST.get('task2')
        update.task3 = request.POST.get('task3')
        update.employee_report=True
        update.save()
        return redirect('/employee_home/')
    return render(request, 'employee/update_task.html', {'update': update})
