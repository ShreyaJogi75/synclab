from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages  # Import messages for displaying errors
from django.http import HttpResponseRedirect  # Ensure HttpResponseRedirect is imported

# Create your views here.
def admin_login(request):
    try:
        # If the user is already authenticated, redirect them to the dashboard
        # if request.user.is_authenticated:
        #     return redirect('/dashboard/')
        
        # Handle POST request for login form submission
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Check if the user exists
            user_obj = User.objects.filter(username=username)  # Correct use of 'User' model
            if not user_obj.exists():
                messages.info(request, 'Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Correct reference

            # Authenticate the user
            user_obj = authenticate(username=username, password=password)  # Correct use of 'authenticate'

            # Check if the user is a superuser
            if user_obj and user_obj.is_superuser:
                login(request, user_obj)  # Log the user in
                return redirect('/dashboard/')  # Redirect to the dashboard
            
            # If the password is invalid
            messages.info(request, 'Invalid Password')
            return redirect('/')
        
        # Render the login page for GET request
        return render(request, 'admin_login.html')
    
    except Exception as e:
        # Print the error in the console and return an error page if desired
        print(e)
        return render(request, 'error.html', {'error': str(e)})  # Ensure a response is returned even on error

def dashboard(request):
    return render(request,'admin_login.html')