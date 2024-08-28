# coding: utf-8
from django.contrib.auth.models import User
User.objects.all()
user = User.objects.get(username='shreya')
print(user.is_staff)  # This should print True
