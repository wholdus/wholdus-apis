# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-19 06:25
from __future__ import unicode_literals

from django.db import migrations

def create_order_buyer_address_history(apps, schema_editor):
	
	Order = apps.get_model("orders","Order")
	BuyerAddressHistory = apps.get_model("users", "BuyerAddressHistory")

	orders = Order.objects.filter(buyer_address_history=None)

	for orderPtr in orders:
		try:
			buyerAddressHistoryPtr = BuyerAddressHistory.objects.filter(buyer=orderPtr.buyer).latest('created_at')
		except Exception, e:
			buyerAddressHistoryPtr = None
		orderPtr.buyer_address_history = buyerAddressHistoryPtr
		orderPtr.save()


class Migration(migrations.Migration):

	dependencies = [
		('orders', '0017_order_buyer_address_histroy'),
		('users', '0031_auto_20160819_0612')
	]

	operations = [
		migrations.RunPython(create_order_buyer_address_history),
	]