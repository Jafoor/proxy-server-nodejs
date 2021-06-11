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
        required = True,
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
                'required' : True
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

class Organization_form(forms.Form):

    class Meta:
        model = Organization
        fields = ('org_about', 'socila_link1', 'org_active_member', 'member1_name', 'member1_mobilenumber', 'member1_position', 'member1_nid')

    org_about = forms.CharField(
        label='About Organization',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'onfocus': 'this.placeholder = ''',
                'onblur': "this.placeholder = 'Your organization name'",
                'type':'text',
                'placeholder': 'Your Password',
                'required' : True
            }
        )
    )
