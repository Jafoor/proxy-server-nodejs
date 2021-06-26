from django import forms
from App_Account.models import VerifyPersonBankDetails


class UserBankProfile(forms.ModelForm):

    class Meta:
        model = VerifyPersonBankDetails
        fields = ('nid_card_front', 'nid_card_back', 'bank_name', 'bank_branch', 'account_number', 'account_name')


    bank_name = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'bank_name',
                'id': 'bank_name',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Bank Name'",
                'type':'text',
                'placeholder': 'Bank Name',
                'required' : True
            }
        )
    )

    bank_branch = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'bank_branch',
                'id': 'bank_branch',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Branch name'",
                'type':'text',
                'placeholder': 'Branch name',
                'required' : True
            }
        )
    )

    account_name = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'account_name',
                'id': 'account_name',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Account name'",
                'type':'text',
                'placeholder': 'Account name',
                'required' : True
            }
        )
    )

    account_number = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'account_number',
                'id': 'account_number',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Enter your account number'",
                'type':'tel',
                'placeholder': 'Enter your account number',
                'required' : True
            }
        )
    )

    nid_card_front = forms.FileField(
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

    nid_card_back = forms.FileField(
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
    
