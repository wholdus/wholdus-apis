# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160719_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover_photo',
            field=models.TextField(blank=True),
        ),
    ]