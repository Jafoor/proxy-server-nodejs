# Generated by Django 3.2.3 on 2021-06-13 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Account', '0005_organization_org_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
