# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-08 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20160808_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitemhistory',
            name='cart',
        ),
        migrations.AddField(
            model_name='cartitemhistory',
            name='shipping_charge',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='cartitemhistory',
            name='subcart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.SubCart'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='pieces',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subcart',
            name='pieces',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subcart',
            name='product_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
