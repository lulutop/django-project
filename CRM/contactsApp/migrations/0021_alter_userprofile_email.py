# Generated by Django 4.2.1 on 2023-09-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactsApp', '0020_alter_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=64, null=True),
        ),
    ]
