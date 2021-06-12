from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.forms import PasswordResetForm
from .models import Organization

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Password confirmation', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")

        return password2

    def save(self, commit = True):
        user = super().save(commit= False)
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()

        return user



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'email',
                'id': 'email',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Email Address'",
                # 'id': 'email',
                'type':'email',
                'placeholder': 'ex: xyz@yourdomain.com',
                'required' : True
            }
        )
    )

    first_name = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'first_name',
                'id': 'first_name',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Enter First Name'",
                # 'id': 'email',
                'type':'text',
                'placeholder': 'Ex: Abu Jafor',
                'required' : True
            }
        )
    )

    last_name = forms.CharField(
        required = False,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'last_name',
                'id': 'last_name',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Enter First Name'",
                # 'id': 'email',
                'type':'text',
                'placeholder': 'Ex: Saleh',
                'required' : False
            }
        )
    )

    password1 = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'password1',
                'id': 'password1',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Enter Password'",
                # 'id': 'email',
                'type':'password',
                'placeholder': '******',
                'required' : True
            }
        )
    )

    password2 = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'password2',
                'id': 'password2',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Rewrite Password'",
                # 'id': 'email',
                'type':'password',
                'placeholder': '******',
                'required' : True
            }
        )
    )

    class Meta:
        """Meta Class"""
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

    def clean_email(self):
        error_messages = {
            'duplicate_email': 'Email is already taken'
        }

        email = self.cleaned_data.get('email')

        try:
            User.objects.get(email=email)

            raise forms.ValidationError(
                error_messages['duplicate_email'],
                code = 'duplicate_email',
            )
        except User.DoesNotExist:
            return email

class UserLoginForm(forms.Form):

    email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'email',
                'id': 'email',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Email Address'",
                # 'id': 'email',
                'type':'email',
                'placeholder': 'Email Address',
                'required' : True
            }
        )
    )

    password = forms.CharField(
        label='Password',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'password',
                'id': 'password',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Your Password'",
                'type':'password',
                'placeholder': 'Your Password',
                'required' : True
            }
        )
    )

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(Q(email__iexact=email)).distinct()
        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError("User does not Exist")
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError("Password/Email Incorrect")
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control valid',
        'placeholder': 'Enter Your email adress',
        'onfocus': 'this.placeholder = ''',
        'onblur': "this.placeholder = 'Your Password'",
        'type': 'email',
        'name': 'email',
        'required' : True
        }))

class OrganizationForm(forms.Form):

    class Meta:
        model = Organization
        fields = ('org_about', 'org_pic', 'contact_number', 'socila_link1', 'socila_link2', 'org_active_member', 'org_prove1', 'member1_name', 'member1_mobilenumber', 'member1_position', 'member1_nid_front', 'member1_nid_back')

    org_about = forms.CharField(
        label='About Organization',
        required=False,
        widget = forms.Textarea(
            attrs={
                'class': 'form-control valid',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'About Your organization'",
                'type':'text',
                'placeholder': 'About Your organization',
                'rows': 5,
                'cols': 15,

            }
        )
    )

    org_pic = forms.CharField(
        label='Organization image or Logo',
        widget = forms.TextInput(
            attrs={
                'class': '',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Organization image or Logo'",
                'type':'file',
                'accept':"image/*",
                'placeholder': 'Organization image or Logo',
                'required' : False
            }
        )
    )

    org_prove1 = forms.CharField(
        label='Organization Legal Document',
        widget = forms.TextInput(
            attrs={
                'class': '',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Organization Legal Document'",
                'type':'file',
                'placeholder': 'Organization Legal Document',
                'required' : False
            }
        )
    )

    contact_number = forms.CharField(
        label='Contact Number',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Organization Contact Number'",
                'type':'tel',
                'placeholder': 'Ex: 01846825017',
                'pattern': "[0-9]{11}",
                'required' : True
            }
        )
    )

    org_active_member = forms.CharField(
        label='Total Active Members',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Total Active Members'",
                'type':'number',
                'placeholder': 'Total Active Members',
                'required' : False
            }
        )
    )

    socila_link1 = forms.CharField(
        label='Social Media Link',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Facebook Page Link'",
                'type':'url',
                'placeholder': 'Facebook Page Link(if any)',
                'required' : False
            }
        )
    )

    socila_link2 = forms.CharField(
        label='Social Media Link',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',

                'onblur': "this.placeholder = 'Website Link'",
                'type':'url',
                'placeholder': 'Website Link(if any)',
                'required' : False
            }
        )
    )

    member1_name = forms.CharField(
        label='Active Member Name',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',

                'onblur': "this.placeholder = 'Member1 Name'",
                'type':'text',
                'placeholder': 'Active Member Name',
                'required' : False
            }
        )
    )

    member1_mobilenumber = forms.CharField(
        label='Active Member Name',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',

                'onblur': "this.placeholder = 'Member1 Contact Number'",
                'type':'tel',
                'placeholder': 'Ex: 01846825017',
                'pattern': "[0-9]{11}",
                'required' : False
            }
        )
    )

    member1_position = forms.CharField(
        label='Member1 Position',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',

                'onblur': "this.placeholder = 'Member1 Position'",
                'type':'text',
                'placeholder': 'Member1 Position',
                'required' : False
            }
        )
    )

    member1_nid_front = forms.CharField(
        label='Member1 NID Card Front Page',
        widget = forms.TextInput(
            attrs={
                'class': '',

                'onblur': "this.placeholder = 'Member1 NID Card Front Page'",
                'type':'file',
                'accept':"image/*",
                'placeholder': 'Member1 NID Card Front Page',
                'required' : False
            }
        )
    )

    member1_nid_back = forms.CharField(
        label='Member1 NID Card Front Page',
        widget = forms.TextInput(
            attrs={
                'class': '',

                'onblur': "this.placeholder = 'Member1 NID Card Back Page'",
                'type':'file',
                'accept':"image/*",
                'placeholder': 'Member1 NID Card Back Page',
                'required' : False
            }
        )
    )
