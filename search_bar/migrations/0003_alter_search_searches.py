# Generated by Django 3.2.15 on 2022-08-17 11:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_bar', '0002_rename_searchmodel_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='searches',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), default=list, size=None),
        ),
    ]
