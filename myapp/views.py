from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        user = User.objects.filter(email=email)
        if user:
            messages.error(request, "User Already Exists")
            return redirect('register')
        else:
             if password == cpassword:
                 newuser = User.objects.create(username=username, email=email, password=cpassword)
                 messages.success(request, "User Registered Successfully")
                 return redirect('login')
             else:
                 messages.error(request, "Password and Confirm Password do not match")
                 return redirect('register')
    return render(request, 'register.html')

def index9(request):
    return render(request, 'index9.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def help(request):
    return render(request, 'help.html')

def projects(request):
    return render(request, 'projects.html')

def errorpage(request):
    return render(request, '404.html')

def registerpage(request):
    return render(request,'register.html')

def LoginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['username'] = user.username
                request.session['email'] = user.email
                return redirect('projects')
            else:
                messages.error(request, "Incorrect password")
                return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "User does not exist")
            return redirect('login')
    return render(request, 'login.html')
