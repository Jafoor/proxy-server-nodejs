from django import forms
from django.contrib.auth import get_user_model
from App_Account.models import Organization
from App_Admin.models import Issue, Contactus
User = get_user_model()

class OrganizationConfirm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ('message', 'is_verified', 'banned')

    message = forms.CharField(
        required = False,
        widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'type':'text',
                'cols': 40,
                'rows': 4,
                'placeholder': 'Message for Organization',
                'required' : False
            }
        )
    )

    is_verified = forms.BooleanField(required=False)
    banned = forms.BooleanField(required=False)

class IssueConfirm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('read', 'solved', 'status')

    read = forms.BooleanField(required=False)
    solved = forms.BooleanField(required=False)
    status = forms.BooleanField(required=False)

class ContactusDetails(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('contacted',)

    contacted = forms.BooleanField(required=False)
