# Generated by Django 3.2.3 on 2021-06-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Event', '0010_auto_20210626_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]
