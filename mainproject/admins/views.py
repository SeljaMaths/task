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
    return render(request,'admin_home.html')


def create_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if name and email and password is not None:
            try:
                employee(name=name, email=email,password=password).save()
                messages.info(request, "successfully created employee account")
                return redirect('/company_login/')
            except:
                pass
        else:
             messages.info(request, "Fields Should not be empty")

        return render(request, 'admins/admin_home.html')