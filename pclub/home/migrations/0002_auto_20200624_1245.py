# Generated by Django 3.0.7 on 2020-06-24 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcements',
            old_name='announcemnt',
            new_name='announcement',
        ),
    ]