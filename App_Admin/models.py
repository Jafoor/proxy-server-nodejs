from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings
# Create your models here.

class LandingPage(models.Model):

    mainTitle = models.CharField(blank=True, null=True, max_length=255)
    sortTitle = models.CharField(blank=True, null=True, max_length=255)
    backgroundImage = models.ImageField(upload_to='landing_page')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.date)

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
        return str(self.email)

class Contactus(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=255, null=True, blank=True)

class SupportedBanks(models.Model):

    name = models.CharField(max_length=255, unique=True)
    active =models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)
