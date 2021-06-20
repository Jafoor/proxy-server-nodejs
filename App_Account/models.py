from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
import hashlib
from django.template import defaultfilters
from django_resized import ResizedImageField
from django.utils.text import slugify
from unidecode import unidecode
import os


def upload_to_org_pic(instance, filename):
    return 'images/%s/org_pic/%s' % (instance.org.email, filename)
def upload_to_member1_nid_front(instance, filename):
    return 'images/%s/member1_nid_front/%s' % (instance.org.email, filename)
def upload_to_org_member1_nid_back(instance, filename):
    return 'images/%s/member1_nid_back/%s' % (instance.org.email, filename)
def upload_to_org_member2_nid_front(instance, filename):
    return 'images/%s/member2_nid_front/%s' % (instance.org.email, filename)
def upload_to_org_member2_nid_back(instance, filename):
    return 'images/%s/member2_nid_back/%s' % (instance.org.email, filename)
def upload_to_org_org_prove1(instance, filename):
    return 'images/%s/org_prove1/%s' % (instance.org.email, filename)
def upload_to_org_org_prove2(instance, filename):
    return 'images/%s/org_prove2/%s' % (instance.org.email, filename)

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, first_name, last_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, first_name, last_name, password, **other_fields)

    def create_user(self, email, first_name, last_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_org = models.BooleanField(default=False)
    is_personorg = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email

    def save(self,force_insert=False, force_update=False, *args, **kwargs):

        if self.slug == None:
            slug = defaultfilters.slugify(unidecode(self.first_name))

            has_slug = CustomUser.objects.filter(slug=slug).exists()

            count = 1

            while has_slug:
                slug = defaultfilters.slugify(unidecode(self.first_name)) + '-' + str(count)
                has_slug = CustomUser.objects.filter(slug=slug).exists()

            self.slug = slug
        super().save(force_insert=False, force_update=False,*args, **kwargs)

class EmailConfirmation(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=500)
    email_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = 'User Email-Confirmed'


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = ResizedImageField(size=[294, 313], crop=['middle', 'center'], upload_to='profilePicture', null=True, blank=True)
    bio = models.CharField(max_length=100, blank=True)
    division = models.CharField(max_length=30, blank=True)
    zilla = models.CharField(max_length=30, blank=True)
    thana = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=500, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user + "'s Profile"

    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]

        for field_name in fields_names:
            value = getattr(self, field_name)
            if value is None or value=='':
                return False
        return True

class VerifyPersonBankDetails(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nid_card_front = models.ImageField(upload_to="nid_card_front", blank=True)
    nid_card_back = models.ImageField(upload_to="nid_card_back", blank=True)
    bank_name = models.CharField(max_length=255, blank=True)
    bank_branch = models.CharField(max_length=255, blank=True)
    account_number = models.CharField(max_length=30, blank=True)
    account_name = models.CharField(max_length=100, blank=True)
    current_balance = models.IntegerField(default=0)
    total_withdraw = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

class Organization(models.Model):
    org = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=255, blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    org_pic = ResizedImageField(size=[293, 313], crop=['middle', 'center'], upload_to=upload_to_org_pic, quality=100, default='default_pic.jpeg', null=True, blank=True)
    org_about = models.TextField(blank=True)
    org_type = models.CharField(blank=True, max_length=255)
    org_active_member = models.IntegerField(default=0)
    division = models.CharField(max_length=30, blank=True)
    zilla = models.CharField(max_length=30, blank=True, null=True)
    thana = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True)
    socila_link1 = models.TextField(blank=True)
    socila_link2 = models.TextField(blank=True)
    given_org_details = models.BooleanField(default=False)
    member1_name = models.CharField(max_length=50, blank=True)
    member1_mobilenumber = models.CharField(max_length=15, blank=True)
    member1_position = models.CharField(max_length=50, blank=True)
    member1_nid_front = models.ImageField(upload_to=upload_to_member1_nid_front, blank=True)
    member1_nid_back = models.ImageField(upload_to=upload_to_org_member1_nid_back, blank=True)
    member2_name = models.CharField(max_length=50, blank=True)
    member2_mobilenumber = models.CharField(max_length=15, blank=True)
    member2_position = models.CharField(max_length=50, blank=True)
    member2_nid_front = models.ImageField(upload_to=upload_to_org_member2_nid_front, blank=True)
    member2_nid_back = models.ImageField(upload_to=upload_to_org_member2_nid_back, blank=True)
    org_prove1 = models.ImageField(upload_to=upload_to_org_org_prove1, blank=True)
    org_prove2 = models.ImageField(upload_to=upload_to_org_org_prove2, blank=True)
    given_org_documents = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.org_name


class VerifyOrgBankDetails(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=255, blank=True)
    bank_branch = models.CharField(max_length=255, blank=True)
    account_number = models.CharField(max_length=30, blank=True)
    account_name = models.CharField(max_length=100, blank=True)
    current_balance = models.IntegerField(default=0)
    total_withdraw = models.IntegerField(default=0)
    total_collection = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

@receiver(post_save, sender=CustomUser)
def organization_creation(sender, instance, created, **kwargd):
    if created and instance.is_org:
        organization = VerifyOrgBankDetails(user=instance)
        organization.save()

@receiver(post_save, sender=CustomUser)
def organization_creation(sender, instance, created, **kwargd):
    if created and instance.is_org:
        organization = Organization(org=instance)
        organization.save()

@receiver(post_save, sender=CustomUser)
def create_user_email_confirmation(sender, instance, created, **kwargd):
    if created:
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        email_confirmed_instance = EmailConfirmation(user=instance)
        user_encode = f'{instance.email}-{dt}'.encode()
        activation_key = hashlib.sha224(user_encode).hexdigest()
        email_confirmed_instance.activation_key = activation_key
        email_confirmed_instance.save()

# @receiver(post_save, sender=CustomUser)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         profile = Profile(user=instance)
#         profile.save()
#
# @receiver(post_save, sender=CustomUser)
# def varify_and_bank_details(sender, instance, created, **kwargs):
#     if created:
#         Varify_and_Bank_Details = VarifyandBankDetails(user=instance)
#         Varify_and_Bank_Details.save()
