# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_product_new_in_product_matrix'),
        ('users', '0014_buyerproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerProductResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_code', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Buyer')),
            ],
        ),
        migrations.CreateModel(
            name='BuyerProductResponseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_code', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Buyer')),
            ],
        ),
        migrations.CreateModel(
            name='BuyerSharedProductID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid_filter_text', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('delete_status', models.BooleanField(default=False)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Buyer')),
            ],
        ),
        migrations.RenameField(
            model_name='buyerproducts',
            old_name='disliked',
            new_name='delete_status',
        ),
        migrations.RemoveField(
            model_name='buyerproducts',
            name='shortlisted',
        ),
        migrations.AddField(
            model_name='buyerproducts',
            name='responded',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='buyerinterest',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category'),
        ),
        migrations.AddField(
            model_name='buyerproductresponsehistory',
            name='buyer_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.BuyerProducts'),
        ),
        migrations.AddField(
            model_name='buyerproductresponsehistory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product'),
        ),
        migrations.AddField(
            model_name='buyerproductresponse',
            name='buyer_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.BuyerProducts'),
        ),
        migrations.AddField(
            model_name='buyerproductresponse',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product'),
        ),
    ]
