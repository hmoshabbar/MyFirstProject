from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class MyApp(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    createted_at=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title
    
class Register(models.Model):
    First_name=models.CharField(max_length=230)
    Last_name=models.CharField(max_length=230)
    Email=models.EmailField(max_length=230)
    Passward=models.CharField(max_length=50)
    Re_Passward=models.CharField(max_length=45)

    def __str__(self):
        return self.First_name
    
    
    
