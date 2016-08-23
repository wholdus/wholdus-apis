# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-18 13:03
from __future__ import unicode_literals

from django.db import migrations

def populateFromBuyerAddress(self, buyerAddressPtr):
	self.buyer_id = buyerAddressPtr.buyer_id
	self.buyeraddress = buyerAddressPtr
	self.pincode = buyerAddressPtr.pincode
	self.address_line = buyerAddressPtr.address_line
	self.landmark = buyerAddressPtr.landmark
	self.city_name = buyerAddressPtr.city_name
	self.state_name = buyerAddressPtr.state_name
	self.country_name = buyerAddressPtr.country_name
	self.contact_number = buyerAddressPtr.contact_number
	self.pincode_number = buyerAddressPtr.pincode_number
	self.priority = buyerAddressPtr.priority

def populateBuyerAddress(buyerAddressPtr, buyeraddress):
	buyerAddressPtr.address_line = buyeraddress["address"]
	buyerAddressPtr.landmark = buyeraddress["landmark"]
	buyerAddressPtr.contact_number = buyeraddress["contact_number"]
	buyerAddressPtr.pincode_number = buyeraddress["pincode"]

	try:
		Pincode = apps.get_model("address", "Pincode")
		pincode = Pincode.objects.get(pincode=buyeraddress["pincode"])
		buyerAddressPtr.pincode = pincode
		buyerAddressPtr.city_name = pincode.city.name
		buyerAddressPtr.state_name = pincode.city.state.name
		buyerAddressPtr.country_name = pincode.city.state.country.name

	except Exception as e:
		buyerAddressPtr.city_name = buyeraddress["city"]
		buyerAddressPtr.state_name = buyeraddress["state"]
		buyerAddressPtr.country_name = "India"

def create_buyer_address_history(apps, schema_editor):

	Buyer = apps.get_model("users", "Buyer")
	BuyerAddress = apps.get_model("users", "BuyerAddress")
	BuyerAddressHistory = apps.get_model("users", "BuyerAddressHistory")

	buyers = Buyer.objects.all()
	for buyerPtr in buyers:

		buyerAddressHistoryPtr = BuyerAddressHistory.objects.filter(buyer=buyerPtr)

		if not buyerAddressHistoryPtr.exists():
			buyerAddressPtr = BuyerAddress.objects.filter(buyer=buyerPtr)
			if len(buyerAddressPtr) == 0:
				buyeraddress["address"] = ""
				buyeraddress["landmark"] = ""
				buyeraddress["contact_number"] = ""
				buyeraddress["pincode"] = ""
				buyeraddress["city"] = ""
				buyeraddress["state"] = ""
				buyerAddressPtr = BuyerAddress(buyer=buyerPtr)
				populateBuyerAddress(buyerAddressPtr, buyeraddress)
				buyerAddressPtr.save()
			else:
				buyerAddressPtr = buyerAddressPtr[0]

			newBuyerAddressHistory = BuyerAddressHistory()
			populateFromBuyerAddress(newBuyerAddressHistory,buyerAddressPtr)
			newBuyerAddressHistory.save()

class Migration(migrations.Migration):

	dependencies = [
		('users', '0029_buyeraddresshistory'),
		('address', '0002_auto_20160719_2241'),

	]

	operations = [
		migrations.RunPython(create_buyer_address_history),
	]