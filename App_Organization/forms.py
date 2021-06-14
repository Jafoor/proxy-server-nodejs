from django import forms
from App_Account.models import VerifyOrgBankDetails

class UpdateOrgBankDetails(forms.ModelForm):

    class Meta:
        model = VerifyOrgBankDetails
        fields = ('bank_name', 'bank_branch', 'account_number', 'account_name',)
