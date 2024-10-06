from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path('', admin_signin, name="admin_signin"),
    path('admin_login_action/', admin_login, name="admin_login"),
    path('dashboard/', dashboard, name="admin_dashboard"),
=======
    path('', views.admin_login, name="admin_login")
>>>>>>> Stashed changes
]
 