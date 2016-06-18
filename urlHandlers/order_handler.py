from django.views.decorators.csrf import csrf_exempt

from orders.views import order
from scripts.utils import customResponse, get_token_payload
import jwt as JsonWebToken

@csrf_exempt
def order_shipment_details(request):

	if request.method == "GET":

		orderShipmentParameters = populateParameters(request)

		if orderShipmentParameters["isSeller"] == 0 and orderShipmentParameters["isInternalUser"] == 0:
			return customResponse("4XX", {"error": "Authentication failure"})

		return order.get_order_shipment_details(request,orderShipmentParameters)
	elif request.method == "POST":
		return order.post_new_order_shipment(request)
	elif request.method == "PUT":
		return order.update_order_shipment(request)

	return customResponse("4XX", {"error": "Invalid request"})

@csrf_exempt
def suborder_details(request):

	if request.method == "GET":

		subOrderParameters = populateParameters(request)

		if subOrderParameters["isSeller"] == 0 and subOrderParameters["isInternalUser"] == 0:
			return customResponse("4XX", {"error": "Authentication failure"})

		return order.get_suborder_details(request,subOrderParameters)
	elif request.method == "PUT":
		return order.update_suborder(request)

	return customResponse("4XX", {"error": "Invalid request"})

@csrf_exempt
def order_details(request):

	if request.method == "GET":

		orderParameters = populateParameters(request)

		if orderParameters["isBuyer"] == 0 and orderParameters["isInternalUser"] == 0:
			return customResponse("4XX", {"error": "Authentication failure"})

		return order.get_order_details(request,orderParameters)
	elif request.method == "POST":
		return order.post_new_order(request)

	return customResponse("4XX", {"error": "Invalid request"})

@csrf_exempt
def order_item_details(request):

	if request.method == "GET":

		orderItemParameters = populateParameters(request)

		if orderItemParameters["isSeller"] == 0 and orderItemParameters["isInternalUser"] == 0:
			return customResponse("4XX", {"error": "Authentication failure"})

		return order.get_order_item_details(request,orderItemParameters)
	elif request.method == "DELETE":
		return order.cancel_order_item(request)

	return customResponse("4XX", {"error": "Invalid request"})

@csrf_exempt
def buyer_payment_details(request):

	if request.method == "GET":

		buyerPaymentParameters = populateParameters(request)

		if buyerPaymentParameters["isBuyer"] == 0 and buyerPaymentParameters["isInternalUser"] == 0:
			return customResponse("4XX", {"error": "Authentication failure"})

		return order.get_buyer_payment_details(request,buyerPaymentParameters)
	elif request.method == "POST":
		return order.post_new_buyer_payment(request)


	return customResponse("4XX", {"error": "Invalid request"})

@csrf_exempt
def seller_payment_details(request):

	if request.method == "GET":

		sellerPaymentParameters = populateParameters(request)

		if sellerPaymentParameters["isSeller"] == 0 and sellerPaymentParameters["isInternalUser"] == 0:
			return customResponse("4XX", {"error": "Authentication failure"})

		return order.get_seller_payment_details(request,sellerPaymentParameters)
	elif request.method == "POST":
		return order.post_new_seller_payment(request)

	return customResponse("4XX", {"error": "Invalid request"})

def populateParameters(request):

	parameters = {}

	accessToken = request.GET.get("access_token", "")

	sellerID = request.GET.get("sellerID", "")

	buyerID = request.GET.get("buyerID", "")

	orderID = request.GET.get("orderID", "")
	orderStatus = request.GET.get("order_status", "")
	orderPaymentStatus = request.GET.get("order_payment_status", "")

	subOrderID = request.GET.get("suborderID", "")
	subOrderStatus = request.GET.get("sub_order_status", "")
	subOrderPaymentStatus = request.GET.get("sub_order_payment_status", "")

	orderShipmentID = request.GET.get("ordershipmentID", "")
	orderShipmentStatus = request.GET.get("order_shipment_status", "")
	
	orderItemID = request.GET.get("orderitemID", "")
	orderItemStatus = request.GET.get("order_item_status", "")

	buyerPaymentID = request.GET.get("buyerpaymentID", "")
	buyerPaymentStatus = request.GET.get("buyer_payment_status", "")

	sellerPaymentID = request.GET.get("sellerpaymentID", "")
	sellerPaymentStatus = request.GET.get("seller_payment_status", "")
	
	
	tokenPayload = get_token_payload(accessToken, "sellerID")
	parameters["isSeller"] = 0
	if "sellerID" in tokenPayload and tokenPayload["sellerID"]!=None:
		parameters["sellersArr"] = [tokenPayload["sellerID"]]
		parameters["isSeller"] = 1
	elif sellerID != "":
		parameters["sellersArr"] = [int(e) if e.isdigit() else e for e in sellerID.split(",")]
	
	tokenPayload = get_token_payload(accessToken, "buyerID")
	parameters["isBuyer"] = 0
	if "buyerID" in tokenPayload and tokenPayload["buyerID"]!=None:
		parameters["buyersArr"] = [tokenPayload["buyerID"]]
		parameters["isBuyer"] = 1
	elif buyerID != "":
		parameters["buyersArr"] = [int(e) if e.isdigit() else e for e in buyerID.split(",")]

	tokenPayload = get_token_payload(accessToken, "internaluserID")
	parameters["isInternalUser"] = 0
	if "internaluserID" in tokenPayload and tokenPayload["internaluserID"]!=None:
		parameters["internalusersArr"] = [tokenPayload["internaluserID"]]
		parameters["isInternalUser"] = 1

	if orderID != "":
		parameters["orderArr"] = [int(e) if e.isdigit() else e for e in orderID.split(",")]
	if orderStatus != "":
		parameters["orderStatusArr"] = [int(e) if e.isdigit() else e for e in orderStatus.split(",")]
	if orderPaymentStatus != "":
		parameters["orderPaymentStatusArr"] = [int(e) if e.isdigit() else e for e in orderPaymentStatus.split(",")]

	if subOrderID != "":
		parameters["subOrderArr"] = [int(e) if e.isdigit() else e for e in subOrderID.split(",")]
	if subOrderStatus != "":
		parameters["subOrderStatusArr"] = [int(e) if e.isdigit() else e for e in subOrderStatus.split(",")]
	if subOrderPaymentStatus != "":
		parameters["subOrderPaymentStatusArr"] = [int(e) if e.isdigit() else e for e in subOrderPaymentStatus.split(",")]
	
	if orderShipmentID != "":
		parameters["orderShipmentArr"] = [int(e) if e.isdigit() else e for e in orderShipmentID.split(",")]
	if orderShipmentStatus != "":
		parameters["orderShipmentStatusArr"] = [int(e) if e.isdigit() else e for e in orderShipmentStatus.split(",")]
	
	if orderItemID != "":
		parameters["orderItemArr"] = [int(e) if e.isdigit() else e for e in orderItemID.split(",")]
	if orderItemStatus != "":
		parameters["orderItemStatusArr"] = [int(e) if e.isdigit() else e for e in orderItemStatus.split(",")]

	if buyerPaymentID != "":
		parameters["buyerPaymentArr"] = [int(e) if e.isdigit() else e for e in buyerPaymentID.split(",")]
	if buyerPaymentStatus != "":
		parameters["buyerPaymentStatusArr"] = [int(e) if e.isdigit() else e for e in buyerPaymentStatus.split(",")]

	if sellerPaymentID != "":
		parameters["sellerPaymentArr"] = [int(e) if e.isdigit() else e for e in sellerPaymentID.split(",")]
	if sellerPaymentStatus != "":
		parameters["sellerPaymentStatusArr"] = [int(e) if e.isdigit() else e for e in sellerPaymentStatus.split(",")]	

	return parameters