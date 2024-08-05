from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index9, name='home'),  # Root URL maps to the index view
    path('in', views.index9, name='index9'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('errorpage/', views.errorpage, name='errorpage'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('projects/', views.projects, name='projects'),
]
