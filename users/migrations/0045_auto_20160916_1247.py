# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-16 12:47
from __future__ import unicode_literals

from django.db import migrations

def create_seller_category(apps, schema_editor):

	Product = apps.get_model("catalog", "Product")
	SellerCategory = apps.get_model("users", "SellerCategory")

	products = Product.objects.all()

	myset = list(set(products.values_list('seller_id', 'category_id')))

	tocreate = []

	for setitem in myset:
		newSellerCategory = SellerCategory(seller_id=setitem[0], category_id=setitem[1])
		tocreate.append(newSellerCategory)

	SellerCategory.objects.bulk_create(tocreate, batch_size=1000)
	

class Migration(migrations.Migration):

	dependencies = [
		('users', '0044_sellercategory'),
		('catalog', '0013_auto_20160719_2241')
	]

	operations = [
		migrations.RunPython(create_seller_category),
	]