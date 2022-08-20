# Generated by Django 3.2.15 on 2022-08-20 15:50

import autoslug.fields
import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(max_length=320, unique=True)),
                ('d_o_b', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=200)),
                ('avatar', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='avatar')),
                ('background', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='background')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='user', unique=True)),
                ('follows', models.ManyToManyField(blank=True, related_name='user_followers', to='profiles.Profile')),
                ('friends', models.ManyToManyField(blank=True, related_name='_profiles_profile_friends_+', to='profiles.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
