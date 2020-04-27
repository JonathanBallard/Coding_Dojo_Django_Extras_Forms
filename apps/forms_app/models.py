
from django.core.exceptions import ValidationError
from django.db import models 
import re 
 
# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 

# Validator Functions
def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than 2'.format(value)
        )

def validateIntegerLessThan200(value):
    if value > 200:
        raise ValidationError(
            '{} must be less than 200'.format(value)
        )

def validateIntegerGreaterThan1(value):
    if value < 1:
        raise ValidationError(
            '{} must be more than 1'.format(value)
        )



class Cat(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Dog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Animal(models.Model):
    name = models.CharField(max_length=255, validators = [validateLengthGreaterThanTwo])
    desc = models.TextField(max_length=1000)
    color = models.CharField(max_length=45)
    age = models.IntegerField(validators = [validateIntegerLessThan200, validateIntegerGreaterThan1])
    weight = models.IntegerField(validators = [validateIntegerLessThan200])
    height = models.IntegerField(validators = [validateIntegerLessThan200])
    animal_type = models.CharField(max_length=100, validators = [validateLengthGreaterThanTwo])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)










