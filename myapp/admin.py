from django.contrib import admin
from .models import *
from django.contrib.sessions.models import Session


# Register your models here.
admin.site.register(Profile)
admin.site.register(ContactMessage)
admin.site.register(OTP)
admin.site.register(NotificationModel)