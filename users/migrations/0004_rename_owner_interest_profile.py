# Generated by Django 4.1.7 on 2023-03-21 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_interests_interest_owner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interest',
            old_name='owner',
            new_name='profile',
        ),
    ]
