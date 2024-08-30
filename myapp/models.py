from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.utils import timezone
# Create your models here.

class Profile(models.Model):  # Renaming your model to avoid conflicts
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # You can add additional fields here
    
class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        self.otp_code = ''.join(random.choices(string.digits, k=6))
        self.save()

    def is_valid(self):
        # OTP is valid for 10 minutes
        return (timezone.now() - self.created_at).seconds < 600