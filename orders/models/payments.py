from django.db import models
from django.contrib import admin
from users.models.seller import *
from users.models.internalUser import *
from users.models.buyer import *
from .subOrder import SubOrder
from .orderShipment import OrderShipment
from .order import Order
from .orderItem import OrderItem

from scripts.utils import validate_date_time, validate_integer, validate_number, validate_bool, link_to_foreign_key
from decimal import Decimal

from django.utils import timezone

class BuyerPayment(models.Model):

	order = models.ForeignKey('orders.Order')
	order_shipment = models.ForeignKey('orders.OrderShipment',null=True,blank=True)

	payment_status = models.IntegerField(default=0)
	payment_method = models.IntegerField(default = 0)
	reference_number = models.CharField(max_length=255, blank=True)
	payment_time = models.DateTimeField(blank=True, null=True)
	details = models.TextField(blank=True)

	payment_value = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-id"]
		default_related_name = "buyerpayment"
		verbose_name="Buyer Payment"
		verbose_name_plural = "Buyer Payments"

	def __unicode__(self):
		return "{} - {} - {}".format(self.id,self.order.display_number,self.order.buyer.name)

	def populateFromCheckout(self,checkoutPtr, cartPtr):
		self.payment_method = checkoutPtr.payment_method
		self.payment_value = cartPtr.final_price
		self.payment_time = timezone.now()

class BuyerPaymentAdmin(admin.ModelAdmin):
	search_fields = ["order__display_number"]
	list_display = ["id", "link_to_order","payment_status", "reference_number", "payment_value"]

	list_display_links = ["id","link_to_order"]

	list_filter = ["payment_status"]

	def link_to_order(self, obj):
		return link_to_foreign_key(obj, "order")
	link_to_order.short_description = "Order"
	link_to_order.allow_tags=True

class SellerPayment(models.Model):

	suborder = models.ForeignKey('orders.SubOrder')

	payment_status = models.IntegerField(default=0)
	payment_method = models.IntegerField(default=0)
	reference_number = models.CharField(max_length=255, blank=True)
	payment_time = models.DateTimeField(blank=True, null=True)
	details = models.TextField(blank=True)

	payment_value = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-id"]
		default_related_name = "sellerpayment"
		verbose_name="Seller Payment"
		verbose_name_plural = "Seller Payments"

	def __unicode__(self):
		return "{} - {} - {}".format(self.id,self.suborder.display_number,self.suborder.seller.name)

class SellerPaymentAdmin(admin.ModelAdmin):
	search_fields = ["suborder__display_number"]
	list_display = ["id", "link_to_suborder","payment_status", "reference_number", "payment_value"]

	list_display_links = ["id","link_to_suborder"]

	list_filter = ["payment_status"]

	def link_to_suborder(self, obj):
		return link_to_foreign_key(obj, "suborder")
	link_to_suborder.short_description = "Suborder"
	link_to_suborder.allow_tags=True

def validateBuyerPaymentData(buyerPayment):

	if not "payment_method" in buyerPayment or not validate_integer(buyerPayment["payment_method"]):
		return False
	if not "reference_number" in buyerPayment or buyerPayment["reference_number"]==None:
		return False
	if not "details" in buyerPayment or buyerPayment["details"]==None:
		buyerPayment["details"] = ""
	if not "payment_time" in buyerPayment or not validate_date_time(buyerPayment["payment_time"]):
		return False
	if not "payment_value" in buyerPayment or not validate_number(buyerPayment["payment_value"]):
		return False
	if not "fully_paid" in buyerPayment or not validate_bool(buyerPayment["fully_paid"]):
		return False

	return True

def populateBuyerPayment(BuyerPaymentPtr, buyerPayment):
	BuyerPaymentPtr.payment_method = int(buyerPayment["payment_method"])
	BuyerPaymentPtr.reference_number = buyerPayment["reference_number"]
	BuyerPaymentPtr.details = buyerPayment["details"]
	BuyerPaymentPtr.payment_time = buyerPayment["payment_time"]
	BuyerPaymentPtr.payment_value = Decimal(buyerPayment["payment_value"])
	BuyerPaymentPtr.payment_status = 1

def validateSellerPaymentData(sellerPayment):

	if not "payment_method" in sellerPayment or not validate_integer(sellerPayment["payment_method"]):
		return False
	if not "reference_number" in sellerPayment or sellerPayment["reference_number"]==None:
		return False
	if not "details" in sellerPayment or sellerPayment["details"]==None:
		sellerPayment["details"] = ""
	if not "payment_time" in sellerPayment or not validate_date_time(sellerPayment["payment_time"]):
		return False
	if not "payment_value" in sellerPayment or not validate_number(sellerPayment["payment_value"]):
		return False
	if not "fully_paid" in sellerPayment or not validate_bool(sellerPayment["fully_paid"]):
		return False

	return True

def populateSellerPayment(SellerPaymentPtr, sellerPayment):
	SellerPaymentPtr.payment_method = int(sellerPayment["payment_method"])
	SellerPaymentPtr.reference_number = sellerPayment["reference_number"]
	SellerPaymentPtr.details = sellerPayment["details"]
	SellerPaymentPtr.payment_time = sellerPayment["payment_time"]
	SellerPaymentPtr.payment_value = Decimal(sellerPayment["payment_value"])
	SellerPaymentPtr.payment_status = 1

def filterSellerPayment(sellerPaymentParameters):
	sellerPayments = SellerPayment.objects.all()

	if "sellerPaymentArr" in sellerPaymentParameters:
		sellerPayments = sellerPayments.filter(id__in=sellerPaymentParameters["sellerPaymentArr"])

	if "sellerPaymentStatusArr" in sellerPaymentParameters:
		sellerPayments = sellerPayments.filter(payment_status__in=sellerPaymentParameters["sellerPaymentStatusArr"])

	if "sellersArr" in sellerPaymentParameters:
		sellerPayments = sellerPayments.filter(suborder__seller_id__in=sellerPaymentParameters["sellersArr"])

	if "subOrderArr" in sellerPaymentParameters:
		sellerPayments = sellerPayments.filter(suborder_id__in=sellerPaymentParameters["subOrderArr"])

	return sellerPayments

def filterBuyerPayment(buyerPaymentParameters):
	buyerPayments = BuyerPayment.objects.all()

	if "buyerPaymentArr" in buyerPaymentParameters:
		buyerPayments = buyerPayments.filter(id__in=buyerPaymentParameters["buyerPaymentArr"])

	if "buyerPaymentStatusArr" in buyerPaymentParameters:
		buyerPayments = buyerPayments.filter(payment_status__in=buyerPaymentParameters["buyerPaymentStatusArr"])

	if "buyersArr" in buyerPaymentParameters:
		buyerPayments = buyerPayments.filter(order__buyer_id__in=buyerPaymentParameters["buyersArr"])

	if "orderArr" in buyerPaymentParameters:
		buyerPayments = buyerPayments.filter(order_id__in=buyerPaymentParameters["orderArr"])

	return buyerPayments

def validateSellerPaymentItemsData(orderItems, subOrderID):

	if len(orderItems) == 0:
		return False

	for orderItem in orderItems:

		if not "orderitemID" in orderItem or not validate_integer(orderItem["orderitemID"]):
			return False

		orderItemPtr = OrderItem.objects.filter(id=int(orderItem["orderitemID"]))
		if len(orderItemPtr) == 0:
			return False

		orderItemPtr = orderItemPtr[0]

		if orderItemPtr.current_status == 4:
			return False

		if orderItemPtr.seller_payment != None:
			return False

		if orderItemPtr.suborder_id != subOrderID:
			return False

	return True

SellerPaymentStatus = {
	0:{"display_value":"Not Paid"},
	1:{"display_value":"Paid"}
}

SellerPaymentMethod = {
	0:{"display_value":"NEFT"},
	1:{"display_value":"IMPS"},
	2:{"display_value":"RTGS"}
}

BuyerPaymentStatus = {
	0:{"display_value":"Not Paid"},
	1:{"display_value":"Paid"},
	2:{"display_value":"Partially Paid"}
}

BuyerPaymentMethod = {
	0:{"display_value":"COD"},
	1:{"display_value":"NEFT"},
	2:{"display_value":"Demand Draft"},
	3:{"display_value":"Cash deposit"},
	4:{"display_value":"Cheque"},
	5:{"display_value":"Debit Card"},
	6:{"display_value":"Credit Card"},
	7:{"display_value":"Net Banking"},
	8:{"display_value":"Wallet"},
	9:{"display_value":"Credit"}
}
