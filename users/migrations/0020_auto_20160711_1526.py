# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-11 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_buyerproducts_shared_on_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstype',
            name='can_be_buyer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='businesstype',
            name='can_be_seller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='businesstype',
            name='can_buyer_buy_from',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='buyerbuysfrom',
            name='delete_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='buyerpurchasingstate',
            name='delete_status',
            field=models.BooleanField(default=False),
        ),
    ]
