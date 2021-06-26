from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
from django.template import defaultfilters
from django.utils.text import slugify
from unidecode import unidecode


def upload_to_event(instance, filename):
    return 'images/%s/%s/events/%s' % (instance.user.pk, instance.user.first_name, filename)

def upload_to_event_extraimage(instance, filename):
    return 'images/%s/%s/eventextraimage/%s' % (instance.user.pk, instance.user.first_name, filename)

class EventType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return (self.name)

def get_deadline():
    return datetime.today() + timedelta(days=15)

class Event(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    event_type =  models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True)
    need_amount = models.IntegerField(default=100)
    collected = models.IntegerField(default=0)
    event_pic = ResizedImageField(size=[1200, 630], crop=['middle', 'center'], upload_to=upload_to_event, quality=100, default='event_image_main.png', null=True, blank=True)
    sort_description = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(default=timezone.now)
    description = RichTextField(null=True, blank=True)
    note = models.TextField(blank=True, null=True)
    percentage = models.IntegerField(default=4.5)
    endtime = models.DateTimeField(default=get_deadline)
    terms_and_condition = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)
    message = models.TextField(blank=True, null=True)
    clicked = models.IntegerField(default=0)
    keywords = models.TextField(blank=True)
    slug = models.SlugField(null=True, blank=True)
    extra_img1 = ResizedImageField(size=[1200, 630], crop=['middle', 'center'], upload_to=upload_to_event_extraimage, quality=100, default='event_image_main.png', null=True, blank=True)
    extra_img2 = ResizedImageField(size=[1200, 630], crop=['middle', 'center'], upload_to=upload_to_event_extraimage, quality=100, default='event_image_main.png', null=True, blank=True)
    message = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self,force_insert=False, force_update=False, *args, **kwargs):

        if self.slug == None:
            slug = defaultfilters.slugify(unidecode(self.title))

            has_slug = Event.objects.filter(slug=slug).exists()

            count = 1

            while has_slug:
                slug = defaultfilters.slugify(unidecode(self.first_name)) + '-' + str(count)
                has_slug = Event.objects.filter(slug=slug).exists()
                count += 1

            self.slug = slug
        super().save(force_insert=False, force_update=False,*args, **kwargs)


class Donation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=4, default=10050.00)
    date = models.DateTimeField(default=timezone.now)
    method = models.CharField(max_length=255, blank=True, null=True)
    hide_identity = models.BooleanField(default=False)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    orderId = models.CharField(max_length=200, blank=True, null=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.event.title)

class Report(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    contactnumber = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.user.first_name)

class Withdraw(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=4, default=10050.00)
    date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    message = models.CharField(blank=True, null=True, max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(user.first_name)
