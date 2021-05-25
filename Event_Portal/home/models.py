from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    max_no = models.IntegerField()
    person_created = models.ForeignKey(User, on_delete = models.CASCADE)
    banner = models.ImageField(default = 'default1.jpg', upload_to = 'banners')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs = {'pk' : self.pk})