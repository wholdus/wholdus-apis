# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-02 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_auto_20160819_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyerproductresponse',
            name='responded_from',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='buyerproductresponsehistory',
            name='responded_from',
            field=models.IntegerField(default=0),
        ),
    ]
