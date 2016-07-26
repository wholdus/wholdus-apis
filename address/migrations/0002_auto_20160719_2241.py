# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-19 22:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='pincode',
            options={'verbose_name': 'Pincode', 'verbose_name_plural': 'Pincodes'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'State', 'verbose_name_plural': 'States'},
        ),
        migrations.AddField(
            model_name='city',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 19, 22, 40, 58, 434655)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 19, 22, 41, 3, 83139)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 19, 22, 41, 6, 601237)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 19, 22, 41, 11, 246277)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pincode',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 19, 22, 41, 16, 222749)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pincode',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 19, 22, 41, 22, 942099)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 19, 22, 41, 26, 593371)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 19, 22, 41, 29, 345680)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.State'),
        ),
        migrations.AlterField(
            model_name='pincode',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.City'),
        ),
        migrations.AlterField(
            model_name='pincode',
            name='pincode',
            field=models.CharField(db_index=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.Country'),
        ),
    ]
