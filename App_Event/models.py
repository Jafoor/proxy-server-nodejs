from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.


class Profile(models.Model):
    name = models.CharField(null=False, max_length=255)
    division = models.CharField(null=False, max_length=255)
    zilla = models.CharField(null=False, max_length=255)
    upozilla = models.CharField(null=False, max_length=255)
    village_or_ward = models.CharField(null=False, max_length=255)
    home_address = models.CharField(null=False, max_length=255)
    mobile_number = models.CharField(max_length=15, null=False)
    #limitation on diagram?? details required
    banned = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Review:
    event_name = models.CharField(null=False, max_length=255)
    user_name = models.CharField(null=True, max_length=255)  # for annonymous reviews
    comment = models.TextField(null=False, help_text="Tell us what you think about it.")
    value = (
        (1, 'Worst'),
        (2, 'Bad'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    )
    rating = models.IntegerField(choices=value)

    def __str__(self):
        return self.name


class Transaction:
    donor_name = models.CharField(null=False, max_length=255)  # instead of username
    # organization that receives the payment
    receiver_name = models.CharField(null=False, max_length=255)
    amount = models.IntegerField(null=False)
    date = models.DateTimeField(null=False)
    hide_from_user = models.BooleanField(default=False)
    for_event = models.BooleanField(default=False)
    event_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AdminUses:  # this class should be renamed to ledger or something###
    transaction_id = models.CharField( max_length=255)
    amount = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField()
    total_revenue = models.IntegerField()
    revenue_per_transaction = models.IntegerField()
    #this class needs thorough discussion

    def __str__(self):
        return self.name


class Event:
    username_of_event_creator = models.CharField(null=False,max_length=255)
    name_of_organiztion = models.CharField(null=False,max_length=255)
    collection_target = models.IntegerField()
    due_date = models.DateTimeField()
    start_date = models.DateTimeField()
    pause_donation = models.BooleanField(default=False)
    is_verified = models.BooleanField()  # by whom ? what is the purpose of verfication ?###
    event_detail = models.TextField(null=False)  # not in diagram, added for clarity
    # not necessary as link to organization's page will the available on the event page
    organization_detail = models.TextField()
    is_private = models.BooleanField(default=False)
    cover_image = models.ImageField()
    event_title = models.CharField(null=False,max_length=255)
    received_donation_in_percentage = models.IntegerField()
    total_transaction = models.IntegerField()  # is it the number of transaction?

    def __str__(self):
        return self.name


class Report:
    username = models.CharField(null=False,max_length=255)
    eventID = models.IntegerField(null=False)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Withdraw:
    username = models.CharField(null=False,max_length=255)
    eventID = models.IntegerField()
    is_blocked = models.BooleanField(default=False)
    amount = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name