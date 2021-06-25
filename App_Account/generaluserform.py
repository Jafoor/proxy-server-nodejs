from django import forms
from App_Account.models import Profile, VerifyPersonBankDetails


class UserInfo(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio', 'address', 'mobile_number')

    bio = forms.CharField(
        required = False,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'bio',
                'id': 'bio',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Works at ...'",
                'type':'text',
                'placeholder': 'Works at ...',
                'required' : False
            }
        )
    )

    address = forms.CharField(
        required = False,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'address',
                'id': 'address',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Enter Your Adress'",
                'type':'text',
                'placeholder': 'Enter your address',
                'required' : False
            }
        )
    )

    mobile_number = forms.CharField(
        required = False,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'mobile_number',
                'id': 'mobile_number',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Enter Your mobile number'",
                'type':'tel',
                'placeholder': 'Enter your mobile number',
                'required' : False
            }
        )
    )

    profile_pic = forms.FileField(
        required = False,
        widget = forms.FileInput(
            attrs={
                'class': 'form-control valid',
                'type':'file',
                'placeholder': '',
                'accept':"image/*",
                'required' : False
            }
        )
    )
