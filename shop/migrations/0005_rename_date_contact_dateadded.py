# Generated by Django 3.2.2 on 2021-07-01 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='date',
            new_name='dateAdded',
        ),
    ]