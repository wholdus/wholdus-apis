# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-15 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_auto_20161114_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerForgotPasswordToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=11)),
                ('is_active', models.BooleanField(default=True)),
                ('verification_attempts', models.IntegerField(default=0)),
                ('otp_number', models.CharField(blank=True, max_length=10)),
                ('messages_sent', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Buyer Forgot Password Token',
                'verbose_name_plural': 'Buyer Forgot Password Tokens',
            },
        ),
    ]
