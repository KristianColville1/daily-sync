# Generated by Django 3.2.14 on 2022-08-01 11:41

from django.db import migrations
import slugger.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=slugger.fields.AutoSlugField(populate_from='title'),
        ),
    ]
