# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-09 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0061_auto_20170103_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyerfirebasetoken',
            name='delete_status',
            field=models.BooleanField(default=False),
        ),
    ]