# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-09 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_smssent'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=100)),
                ('question', models.TextField(blank=True)),
                ('answer', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]