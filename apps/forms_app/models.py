from django.db import models 
import re 
 
# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 

class Cat(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)