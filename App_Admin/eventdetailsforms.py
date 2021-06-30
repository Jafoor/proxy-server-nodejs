from django import forms
from App_Event.models import Event
from App_Account.models import VerifyPersonBankDetails

class EventDetailsFromAdmin(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('message', 'active', 'keywords', 'banned', 'percentage')
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

    active = forms.BooleanField(required=False)
    banned = forms.BooleanField(required=False)
    percentage = forms.IntegerField(
        required=False,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'number',
                'placeholder': '10000',
                'required' : False
            }
        )
    )

    keywords = forms.CharField(
        required=False,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'text',
                'placeholder': 'keywords',
                'required' : False
            }
        )
    )

class VerifyPerson(forms.ModelForm):
    class Meta:
        model = VerifyPersonBankDetails
        fields = ('message', 'filled', 'is_verified')

    filled = forms.BooleanField(required=False)
    is_verified = forms.BooleanField(required=False)

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
