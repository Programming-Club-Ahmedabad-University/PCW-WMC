# Generated by Django 3.0.7 on 2020-06-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='image',
            field=models.ImageField(upload_to='about/profiles'),
        ),
    ]
