# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-11 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20160808_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cod_charge',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='subcart',
            name='cod_charge',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
