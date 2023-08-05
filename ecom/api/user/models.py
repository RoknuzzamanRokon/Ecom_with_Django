from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default = 'Anonymous')
    email = models.EmailField(max_length=250,unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True,null=True)
    session_token = models.CharField(max_length=10, default=0)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)

    # objects = CustomUserManager()
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
