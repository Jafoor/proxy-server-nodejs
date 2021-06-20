from django.contrib import admin
from App_Event.models import EventType, CreateEvent
# Register your models here.

admin.site.register(EventType)
admin.site.register(CreateEvent)
