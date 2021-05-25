from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from home.models import Event
from django.urls import reverse


# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()
    branch = models.CharField(max_length=100)
    person_created = models.ForeignKey(User, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
