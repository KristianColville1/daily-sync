# Generated by Django 3.2.15 on 2022-08-15 09:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20220811_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='total_likes',
        ),
        migrations.AddField(
            model_name='post',
            name='angry_likes',
            field=models.ManyToManyField(blank=True, related_name='angry_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='heart_likes',
            field=models.ManyToManyField(blank=True, related_name='heart_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='laugh_likes',
            field=models.ManyToManyField(blank=True, related_name='laugh_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbs_likes',
            field=models.ManyToManyField(blank=True, related_name='thumb_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]