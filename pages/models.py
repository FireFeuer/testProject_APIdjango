from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from django.conf import settings 
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.IntegerField()
    building_number = models.CharField(max_length=100)
    class Meta:
        app_label = 'companysAPIdjango'
        db_table = 'address'

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name_company = models.CharField(max_length=100)
    name_person = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    web_link = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    class Meta:
        app_label = 'companysAPIdjango'
        db_table = 'company'




        





   