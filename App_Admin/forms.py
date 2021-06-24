from django import forms
from django.contrib.auth import get_user_model
from App_Account.models import Organization
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
