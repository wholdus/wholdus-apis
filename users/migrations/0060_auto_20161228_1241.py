# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-28 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0059_buyerfirebasetoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerfirebasetoken',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Buyer'),
        ),
    ]