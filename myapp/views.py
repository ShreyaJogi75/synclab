from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordResetForm
import random,string
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import login, update_session_auth_hash

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # Create or update OTP record
            otp_record, created = OTP.objects.get_or_create(user=user)
            otp_record.generate_otp()  # Generate a new OTP
            otp_record.save()

            # Calculate OTP expiry time (10 minutes from now)
            otp_expiry_time = timezone.now() + timezone.timedelta(minutes=10)
            request.session['otp_id'] = otp_record.id
            request.session['otp_email'] = email
            request.session['otp_expiry_time'] = otp_expiry_time.isoformat()

            # Send OTP email
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp_record.otp_code}.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )
            messages.success(request, "OTP sent to your email.")
            return redirect('verify_otp')  # Redirect to OTP verification page
        else:
            messages.error(request, "No account found with this email.")

    return render(request, 'forgot-pass.html')


def verify_otp(request):
    if request.method == 'POST':
        otp_input = request.POST.get('otp')
        otp_id = request.session.get('otp_id')
        
        if otp_id:
            otp_record = OTP.objects.filter(id=otp_id).first()
            if otp_record and otp_record.is_valid() and otp_input == otp_record.otp_code:
                messages.success(request, "OTP verified successfully!")
                otp_record.delete()  # Delete the OTP record after successful verification
                return redirect('reset_password')
            else:
                messages.error(request, "Invalid or expired OTP. Please try again.")
        else:
            messages.error(request, "OTP session expired. Please request a new OTP.")
    
    return render(request, 'verify_otp.html')

def reset_password(request):
    if request.method == 'POST':
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if new_password1 != new_password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'reset_password.html')
        
        email = request.session.get('otp_email')
        otp_expiry_time_str = request.session.get('otp_expiry_time')

        if not email or not otp_expiry_time_str:
            messages.error(request, "Session has expired or is invalid.")
            return redirect('index9')

        try:
            otp_expiry_time = timezone.datetime.fromisoformat(otp_expiry_time_str)
        except ValueError:
            messages.error(request, "Invalid expiry time format.")
            return redirect('index9')

        if timezone.now() > otp_expiry_time:
            messages.error(request, "Session has expired.")
            return redirect('index9')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address.")
            return redirect('index9')

        user = User.objects.filter(email=email).first()
        if user:
            user.set_password(new_password1)
            user.save()
            auth_login(request, user)  # Use the correct alias here
            messages.success(request, "Password reset successfully, and you are logged in.")
            return redirect('projects')
        else:
            messages.error(request, "User not found.")
            return redirect('index9')

    return render(request, 'reset_password.html')


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

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Log the user in
            request.session['username'] = user.username
            request.session['email'] = user.email
            return redirect('projects')
        else:
            messages.error(request, "Invalid username or password")
            request.session['username'] = ""  # Clear session on failure
            return redirect('login')

    return render(request, 'login.html')
