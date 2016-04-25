from users.serializers.seller import serialize_seller, serialize_seller_address
from users.serializers.buyer import serialize_buyer, serialize_buyer_address
from ..models.orderItem import OrderItemStatus

def parseOrderItem(orderItemQuerySet):

	orderItems = []

	for orderItem in orderItemQuerySet:
		orderItemEntry = serializeOrderItem(orderItem)
		orderItems.append(orderItemEntry)

	return orderItems

def serializeOrderItem(orderItemEntry):
	orderItem = {}
	if hasattr(orderItemEntry,"suborder"):
		orderItem["suborder"] = serializeSubOrder(orderItemEntry.suborder)
	if hasattr(orderItemEntry,"order_shipment"):
		orderItem["order_shipment"] = serializeOrderShipment(orderItemEntry.order_shipment)
	if hasattr(orderItemEntry,"seller_payment"):
		orderItem["seller_payment"] = serializeSellerPayment(orderItemEntry.seller_payment)
	orderItem["lots"] = orderItemEntry.lots
	orderItem["undiscounted_price_per_lot"] = orderItemEntry.undiscounted_price_per_lot
	orderItem["discount"] = orderItemEntry.discount
	orderItem["total_price"] = orderItemEntry.total_price
	orderItem["cod_charge"] = orderItemEntry.cod_charge
	orderItem["shipping_charge"] = orderItemEntry.shipping_charge
	orderItem["final_price"] = orderItemEntry.final_price
	orderItem["created_at"] = orderItemEntry.created_at
	orderItem["updated_at"] = orderItemEntry.updated_at
	orderItem["current_status"] = orderItemEntry.current_status
	orderItem["current_status_display_value"] = OrderItemStatus[orderItemEntry.current_status]
	orderItem["cancellation_remarks"] = orderItemEntry.cancellation_remarks
	orderItem["cancellation_time"] = orderItemEntry.cancellation_time
	return orderItem

def serializeSubOrder(subOrderEntry):
	subOrder = {
		"suborderID":subOrderEntry.id,
		"product_count":subOrderEntry.product_count,
		"undiscounted_price":subOrderEntry.undiscounted_price,
		"total_price":subOrderEntry.total_price,
		"seller":serialize_seller(subOrderEntry.seller),
		"order":serializeOrder(subOrderEntry.order)
	}
	return subOrder

def serializeOrder(orderEntry):
	order = {
		"orderID":orderEntry.id,
		"buyer":serialize_buyer(orderEntry.buyer),
		"product_count":orderEntry.product_count,
		"undiscounted_price":orderEntry.undiscounted_price,
		"total_price":orderEntry.total_price,
		"remarks":orderEntry.remarks,
		"created_at":orderEntry.created_at,
		"updated_at":orderEntry.updated_at
	}
	return order

def serializeOrderShipment(orderShipmentEntry):
	orderShipment = {
		"ordershipmentID": orderShipmentEntry.id,
		"pickup": serialize_seller_address(orderShipmentEntry.pickup),
		"drop": serialize_buyer_address(orderShipmentEntry.drop),
		"invoice_number": orderShipmentEntry.invoice_number,
		"invoice_date": orderShipmentEntry.invoice_date,
		"logistics_partner": orderShipmentEntry.logistics_partner,
		"waybill_number": orderShipmentEntry.waybill_number,
		"packaged_weight": orderShipmentEntry.packaged_weight,
		"packaged_length": orderShipmentEntry.packaged_length,
		"packaged_breadth": orderShipmentEntry.packaged_breadth,
		"packaged_height": orderShipmentEntry.packaged_height,
		"remarks": orderShipmentEntry.remarks,
		"tpl_manifested_time": orderShipmentEntry.tpl_manifested_time,
		"tpl_in_transit_time": orderShipmentEntry.tpl_in_transit_time,
		"delivered_time": orderShipmentEntry.delivered_time,
		"rto_in_transit_time": orderShipmentEntry.rto_in_transit_time,
		"rto_delivered_time":		 orderShipmentEntry.rto_delivered_time,
		"rto_remarks": orderShipmentEntry.rto_remarks,
		"created_at": orderShipmentEntry.created_at,
		"updated_at": orderShipmentEntry.updated_at
	}
	return orderShipment

def serializeSellerPayment(sellerPaymentEntry):
	sellerPayment = {
		"sellerpaymentID":sellerPaymentEntry.id,
		"payment_status":sellerPaymentEntry.payment_status,
		"payment_method":sellerPaymentEntry.payment_method,
		"payment_date":sellerPaymentEntry.payment_date,
		"details":sellerPaymentEntry.details
	}
	return sellerPayment