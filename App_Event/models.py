from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField, DateTimeCheckMixin, DateTimeField, IntegerField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.


class Profile(models.Model):
    name = models.CharField(null=False)
    division = models.CharField(null=False)
    zilla = models.CharField(null=False)
    upozilla = models.CharField(null=False)
    village_or_ward = CharField(null=False)
    home_address = CharField(null=False)
    mobile_number = CharField(max_length=15, null=False)
    #limitation on diagram?? details required
    banned = BooleanField(default=False)

    def __str__(self):
        return self.name


class Review:
    event_name = CharField(null=False)
    user_name = CharField(null=True)  # for annonymous reviews
    comment = TextField(
        null=False, help_text="Tell us what you think about it.")
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
    donor_name = CharField(null=False)  # instead of username
    # organization that receives the payment
    receiver_name = CharField(null=False)
    amount = IntegerField(null=False)
    date = DateTimeCheckMixin(null=False)
    hide_from_user = BooleanField(default=False)
    for_event = BooleanField(default=False)
    event_name = CharField(max_length=255)

    def __str__(self):
        return self.name


class AdminUses:  # this class should be renamed to ledger or something###
    transaction_id = CharField()
    amount = IntegerField()
    total = IntegerField()
    date = DateTimeField()
    total_revenue = IntegerField()
    revenue_per_transaction = IntegerField()
    #this class needs thorough discussion

    def __str__(self):
        return self.name


class Event:
    username_of_event_creator = CharField(null=False)
    name_of_organiztion = CharField(null=False)
    collection_target = IntegerField()
    due_date = DateTimeField()
    start_date = DateTimeField()
    pause_donation = BooleanField(default=False)
    is_verified = BooleanField()  # by whom ? what is the purpose of verfication ?###
    event_detail = TextField(null=False)  # not in diagram, added for clarity
    # not necessary as link to organization's page will the available on the event page
    organization_detail = TextField()
    is_private = BooleanField(default=False)
    cover_image = ImageField()
    event_title = CharField(null=False)
    received_donation_in_percentage = IntegerField()
    total_transaction = IntegerField()  # is it the number of transaction?

    def __str__(self):
        return self.name


class Report:
    username = CharField(null=False)
    eventID = IntegerField(null=False)
    description = TextField()
    date = DateTimeField()

    def __str__(self):
        return self.name


class Withdraw:
    username = CharField(null=False)
    eventID = IntegerField()
    is_blocked = BooleanField(default=False)
    amount = IntegerField()
    date = DateTimeField()

    def __str__(self):
        return self.name
