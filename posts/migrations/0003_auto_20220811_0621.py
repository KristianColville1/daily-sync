# Generated by Django 3.2.15 on 2022-08-11 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='post_body',
        ),
    ]
