from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index9, name='home'),  # Root URL maps to the index view
    path('index9/', views.index9, name='index9'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('loginuser/', views.LoginUser, name='loginuser'),
    path('registerpage/', views.registerpage, name='registerpage'),
    path('register/', views.register, name="register"),
    path('errorpage/', views.errorpage, name='errorpage'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('projects/', views.projects, name='projects'),
    path('forgotpw/', auth_views.PasswordResetView.as_view(template_name='forgot-pass.html'), name='forgotpw'),
    path('forgot-password/', views.send_otp, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password/', views.reset_password, name='reset_password'),
]
