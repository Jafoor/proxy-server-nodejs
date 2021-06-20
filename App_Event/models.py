from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField


def upload_to_event(instance, filename):
    return 'images/%s/%s/events/%s' % (instance.user.pk, instance.user.first_name, filename)

def upload_to_event_extraimage(instance, filename):
    return 'images/%s/%s/eventextraimage/%s' % (instance.user.pk, instance.user.first_name, filename)

class EventType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return '%s' % self.name

def get_deadline():
    return datetime.today() + timedelta(days=15)

class CreateEvent(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    event_type =  models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True)
    need_amount = models.IntegerField(default=100000)
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
    extra_img1 = ResizedImageField(size=[1200, 630], crop=['middle', 'center'], upload_to=upload_to_event_extraimage, quality=100, default='event_image_main.png', null=True, blank=True)
    extra_img2 = ResizedImageField(size=[1200, 630], crop=['middle', 'center'], upload_to=upload_to_event_extraimage, quality=100, default='event_image_main.png', null=True, blank=True)

    def __str__(self):
        return self.title
