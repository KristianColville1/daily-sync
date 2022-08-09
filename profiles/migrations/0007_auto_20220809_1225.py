# Generated by Django 3.2.15 on 2022-08-09 12:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='background',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='background'),
        ),
    ]
