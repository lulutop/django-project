# Generated by Django 4.2.1 on 2023-09-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactsApp', '0015_alter_userprofile_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]