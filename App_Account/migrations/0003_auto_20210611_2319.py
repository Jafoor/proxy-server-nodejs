# Generated by Django 3.2.3 on 2021-06-11 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('App_Account', '0002_auto_20210609_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_org',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_personorg',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='VerifyPersonBankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nid_card_front', models.ImageField(blank=True, upload_to='nid_card_front')),
                ('nid_card_back', models.ImageField(blank=True, upload_to='nid_card_back')),
                ('bank_name', models.CharField(blank=True, max_length=255)),
                ('bank_branch', models.CharField(blank=True, max_length=255)),
                ('account_number', models.CharField(blank=True, max_length=30)),
                ('account_name', models.CharField(blank=True, max_length=100)),
                ('current_balance', models.IntegerField(default=0)),
                ('total_withdraw', models.IntegerField(default=0)),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VerifyOrgBankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=255)),
                ('bank_branch', models.CharField(blank=True, max_length=255)),
                ('account_number', models.CharField(blank=True, max_length=30)),
                ('account_name', models.CharField(blank=True, max_length=100)),
                ('current_balance', models.IntegerField(default=0)),
                ('total_withdraw', models.IntegerField(default=0)),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=0, size=[294, 313], upload_to='profilePicture')),
                ('bio', models.CharField(blank=True, max_length=100)),
                ('division', models.CharField(blank=True, max_length=30)),
                ('zilla', models.CharField(blank=True, max_length=30)),
                ('thana', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('mobile_number', models.CharField(blank=True, max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(blank=True, max_length=255)),
                ('org_about', models.TextField(blank=True)),
                ('org_type', models.CharField(blank=True, max_length=255)),
                ('org_active_member', models.IntegerField(default=0)),
                ('division', models.CharField(blank=True, max_length=30)),
                ('zilla', models.CharField(blank=True, max_length=30)),
                ('thana', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('socila_link1', models.TextField(blank=True)),
                ('socila_link2', models.TextField(blank=True)),
                ('member1_name', models.CharField(blank=True, max_length=50)),
                ('member1_mobilenumber', models.CharField(blank=True, max_length=15)),
                ('member1_position', models.CharField(blank=True, max_length=50)),
                ('member1_nid_front', models.ImageField(blank=True, upload_to='member1_nid_front')),
                ('member1_nid_back', models.ImageField(blank=True, upload_to='member1_nid_back')),
                ('member2_name', models.CharField(blank=True, max_length=50)),
                ('member2_mobilenumber', models.CharField(blank=True, max_length=15)),
                ('member2_position', models.CharField(blank=True, max_length=50)),
                ('member2_nid_front', models.ImageField(blank=True, upload_to='member2_nid_front')),
                ('member2_nid_back', models.ImageField(blank=True, upload_to='member2_nid_back')),
                ('org_prove1', models.ImageField(blank=True, upload_to='prove_1')),
                ('org_prove2', models.ImageField(blank=True, upload_to='prove_2')),
                ('is_verified', models.BooleanField(default=False)),
                ('org', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
