from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages  # Import messages for displaying errors
from django.http import HttpResponseRedirect  # Ensure HttpResponseRedirect is imported

# Create your views here.

def admin_signin(request):
    return render(request, 'admin_login.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('/dj-admin/dashboard/')  # Redirect to admin dashboard
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('/dj-admin/')
    else:
            return redirect('/dj-admin/')

def dashboard(request):
    return render(request,'admin_dashboard.html')