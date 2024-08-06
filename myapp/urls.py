from django.urls import path
from . import views

urlpatterns = [
    path('', views.index9, name='home'),  # Root URL maps to the index view
    path('index9/', views.index9, name='index9'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('registerpage/', views.registerpage, name='registerpage'),
    path('register/', views.register, name="register"),
    path('errorpage/', views.errorpage, name='errorpage'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('projects/', views.projects, name='projects'),
]
