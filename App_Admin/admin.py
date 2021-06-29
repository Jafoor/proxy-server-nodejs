from django.contrib import admin
from App_Admin.models import LandingPage, CommonField, Contactus, SupportedBanks
# Register your models here.

admin.site.register(LandingPage)
admin.site.register(CommonField)
admin.site.register(Contactus)
admin.site.register(SupportedBanks)
