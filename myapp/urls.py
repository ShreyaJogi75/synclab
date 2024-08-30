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
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

]
