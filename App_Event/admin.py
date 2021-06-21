from django.contrib import admin
from App_Event.models import EventType, Event, Donation, Report
# Register your models here.

admin.site.register(EventType)
admin.site.register(Event)
admin.site.register(Donation)
admin.site.register(Report)
