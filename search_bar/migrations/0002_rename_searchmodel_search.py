# Generated by Django 3.2.15 on 2022-08-16 18:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search_bar', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SearchModel',
            new_name='Search',
        ),
    ]
