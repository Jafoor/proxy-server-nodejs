from django.contrib import admin
from App_Account.models import VerifyOrgBankDetails
# Register your models here.

class VerifyOrganizationBankDetails(admin.ModelAdmin):

    list_display = ('user', 'bank_name',)

admin.site.register(VerifyOrgBankDetails, VerifyOrganizationBankDetails)
