# Generated by Django 3.2.3 on 2021-06-16 17:58

import App_Account.models
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('App_Account', '0013_alter_organization_org_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='org_pic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='default_pic.jpeg', force_format=None, keep_meta=True, null=True, quality=100, size=[293, 313], upload_to=App_Account.models.upload_to_org_pic),
        ),
    ]
