# Generated by Django 3.2.15 on 2022-08-15 18:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_auto_20220815_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='likes',
            new_name='total_likes',
        ),
        migrations.AddField(
            model_name='comment',
            name='angry_likes',
            field=models.ManyToManyField(blank=True, related_name='comment_angry_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='heart_likes',
            field=models.ManyToManyField(blank=True, related_name='comment_heart_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='laugh_likes',
            field=models.ManyToManyField(blank=True, related_name='comment_laugh_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='thumbs_likes',
            field=models.ManyToManyField(blank=True, related_name='comment_thumb_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
