from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
# Create your models here.

class LandingPage(models.Model):

    mainTitle = models.CharField(blank=True, null=True, max_length=255)
    sortTitle = models.CharField(blank=True, null=True, max_length=255)
    backgroundImage = models.ImageField(upload_to='landing_page')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (self.date)

class CommonField(models.Model):

    email = models.EmailField(blank=True, null=True)
    contactnumber = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(upload_to='logo', blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    youtube = models.TextField(blank=True, null=True)
    other1 = models.TextField(blank=True, null=True)
    other2 = models.TextField(blank=True, null=True)
    footerLogo = models.ImageField(upload_to='logo', blank=True, null=True)
    footernote = models.TextField(blank=True, null=True)

    def __str__(self):
        return (self.email)
