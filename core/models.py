from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass 

class Firm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='firms')
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
