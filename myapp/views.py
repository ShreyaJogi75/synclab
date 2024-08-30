from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists")
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')

        if password == cpassword:
            newuser = User.objects.create_user(username=username, email=email, password=password)
            
            # Create the user's profile
            Profile.objects.create(user=newuser)
            
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

def forgotpasspage(request):
    return render(request,'forgot-pass.html')

def registerpage(request):
    return render(request,'register.html')

def LoginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        request.session['username'] = ""
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Use the aliased login function
            request.session['username'] = user.username
            request.session['email'] = user.email
            return redirect('projects')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')
