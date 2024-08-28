from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):  # Renaming your model to avoid conflicts
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # You can add additional fields here