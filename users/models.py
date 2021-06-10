from django.db import models
from django.contrib.auth.models  import User
from django.db.models.fields import DateField, EmailField
from django.urls import reverse

# Create your models here.

class Person(models.Model):
    fname = models.CharField(max_length=200, null = True)
    user_id = models.CharField(max_length=200, null = True)
    email = EmailField(null=True, max_length=200)
    dob = DateField(null=True )
    
    
    def __str__(self):
        return self.fname

class user_log(User):
    fields = ['username','password','is_active','date_joined','email']
    
    def __str__(self):
        return self.username

