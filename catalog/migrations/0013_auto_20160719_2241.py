# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-19 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_colourtype_fabrictype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['priority', 'id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productdetails',
            options={'verbose_name': 'Product Details', 'verbose_name_plural': 'Product Details'},
        ),
        migrations.AlterModelOptions(
            name='productlot',
            options={'verbose_name': 'Product Lot', 'verbose_name_plural': 'Product Lots'},
        ),
        migrations.AlterField(
            model_name='product',
            name='display_name',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='description',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='sample_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='weight_per_unit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productlot',
            name='lot_size_from',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productlot',
            name='lot_size_to',
            field=models.IntegerField(default=0),
        ),
    ]
