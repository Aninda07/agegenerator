# Generated by Django 4.0.6 on 2022-07-28 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_alter_contact_birthdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Birthdate',
            new_name='Birth_year',
        ),
    ]
