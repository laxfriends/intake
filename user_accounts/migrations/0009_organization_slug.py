# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-18 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0008_add_profiles_related_name_to_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
