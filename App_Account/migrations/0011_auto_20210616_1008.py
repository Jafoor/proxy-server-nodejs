# Generated by Django 3.2.3 on 2021-06-16 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Account', '0010_auto_20210616_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='given_ord_details',
            new_name='given_org_details',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='org_documents_given',
            new_name='given_org_documents',
        ),
    ]
