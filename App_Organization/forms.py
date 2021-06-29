from django import forms
from App_Account.models import Organization
from App_Event.models import Withdraw

class OrgDocumentsSubmit(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ('org_pic', 'member1_name', 'member1_position', 'member1_mobilenumber', 'member1_nid_front', 'member1_nid_back', 'member2_name', 'member2_position', 'member2_mobilenumber', 'member2_nid_front', 'member2_nid_back', 'org_prove1', 'org_prove2')


    org_pic = forms.FileField(
        required = False,
        widget = forms.FileInput(
            attrs={
                'class': 'form-control',
                'type':'file',
                'placeholder': '',
                'accept':"image/*",
                'required' : False
            }
        )
    )

    member1_name = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'text',
                'placeholder': 'Name of First Active Member',
                'required' : True
            }
        )
    )

    member1_position = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'text',
                'placeholder': 'Position of First Active Member',
                'required' : True
            }
        )
    )

    member1_mobilenumber = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'tel',
                'placeholder': 'Contact Number of First Active Member',
                'required' : True
            }
        )
    )

    member1_nid_front = forms.FileField(
        required = False,
        widget = forms.FileInput(
            attrs={
                'class': 'form-control',
                'type':'file',
                'placeholder': '',
                'accept':"image/*",
                'required' : False
            }
        )
    )

    member1_nid_back = forms.FileField(
        required = False,
        widget = forms.FileInput(
            attrs={
                'class': 'form-control',
                'type':'file',
                'placeholder': '',
                'accept':"image/*",
                'required' : False
            }
        )
    )

    member2_name = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'text',
                'placeholder': 'Name of Second Active Member',
                'required' : True
            }
        )
    )

    member2_position = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'text',
                'placeholder': 'Position of Second Active Member',
                'required' : True
            }
        )
    )

    member2_mobilenumber = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'tel',
                'placeholder': 'Contact Number of Second Active Member',
                'required' : True
            }
        )
    )

    member2_nid_front = forms.FileField(
        required = False,
        widget = forms.FileInput(
            attrs={
                'class': 'form-control',
                'type':'file',
                'placeholder': '',
                'accept':"image/*",
                'required' : False
            }
        )
    )

    member2_nid_back = forms.FileField(
        required = False,
        widget = forms.FileInput(
            attrs={
                'class': 'form-control',
                'type':'file',
                'placeholder': '',
                'accept':"image/*",
                'required' : False
            }
        )
    )

    org_prove1 = forms.FileField(
        required = False,
        widget = forms.FileInput(
            attrs={
                'class': 'form-control',
                'type':'file',
                'placeholder': 'if any',
                'accept':"image/*,",
                'required' : False
            }
        )
    )

    org_prove2 = forms.FileField(
        required = False,
        widget = forms.FileInput(
            attrs={
                'class': 'form-control',
                'type':'file',
                'placeholder': 'if any',
                'accept':"image/*",
                'required' : False
            }
        )
    )

class OrgWithdraw(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = ('amount', 'confirm')

    amount = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'number',
                'placeholder': 'Amount you want to withdraw',
                'required' : True
            }
        )
    )

    confirm = forms.BooleanField(
        required = True
    )
