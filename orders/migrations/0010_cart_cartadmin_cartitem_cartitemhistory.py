# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-04 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20160804_1615'),
        ('catalog', '0013_auto_20160719_2241'),
        ('orders', '0009_auto_20160719_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Buyer')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Cart',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lots', models.PositiveIntegerField(default=0)),
                ('pieces', models.PositiveIntegerField(default=0)),
                ('lot_size', models.PositiveIntegerField(default=1)),
                ('retail_price_per_piece', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('calculated_price_per_piece', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('status', models.IntegerField(default=0)),
                ('added_from_shortlist', models.BooleanField(default=0)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Buyer')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
            options={
                'ordering': ['-updated_at'],
                'verbose_name': 'Cart Item',
                'verbose_name_plural': 'Cart Items',
                'default_related_name': 'cartitem',
            },
        ),
        migrations.CreateModel(
            name='CartItemHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lots', models.PositiveIntegerField(default=0)),
                ('pieces', models.PositiveIntegerField(default=0)),
                ('lot_size', models.PositiveIntegerField(default=1)),
                ('retail_price_per_piece', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('calculated_price_per_piece', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('added_from_shortlist', models.BooleanField(default=0)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Buyer')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Cart')),
                ('cartitem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.CartItem')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
            options={
                'verbose_name': 'Cart Item History',
                'verbose_name_plural': 'Cart Item History',
            },
        ),
    ]