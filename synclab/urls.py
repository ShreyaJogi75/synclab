from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-admin/', include('customadmin.urls')),
    path('', include('myapp.urls')),  # Includes your app's URLs at the root level
]
