from django.views.decorators.csrf import csrf_exempt

from orders.views import order
from scripts.utils import customResponse, get_token_payload
import jwt as JsonWebToken

@csrf_exempt
def order_shipment_details(request):

	if request.method == "GET":
		status = request.GET.get("status", "")
		sellerID = request.GET.get("sellerID", "")

		accessToken = request.GET.get("access_token", "")
		tokenPayload = get_token_payload(accessToken, "sellerID")
		isSeller = 0
		if "sellerID" in tokenPayload and tokenPayload["sellerID"]!=None:
			sellersArr = [tokenPayload["sellerID"]]
			isSeller = 1
		elif sellerID == "":
			sellersArr = []
		else:
			sellersArr = [int(e) if e.isdigit() else e for e in sellerID.split(",")]

		tokenPayload = get_token_payload(accessToken, "internaluserID")
		isInternalUser = 0
		internalusersArr = []
		if "internaluserID" in tokenPayload and tokenPayload["internaluserID"]!=None:
			internalusersArr = [tokenPayload["internaluserID"]]
			isInternalUser = 1

		if status == "":
			statusArr = []
		else:
			statusArr = [int(e) if e.isdigit() else e for e in status.split(",")]

		return order.get_order_shipment_details(request,statusArr,sellersArr, isSeller,internalusersArr,isInternalUser)
	elif request.method == "POST":
		return order.post_new_order_shipment(request)
	elif request.method == "PUT":
		return order.update_order_shipment(request)

	return customResponse("4XX", {"error": "Invalid request"})

@csrf_exempt
def suborder_details(request):

	if request.method == "GET":

		subOrderParameters = {}

		status = request.GET.get("status", "")
		sellerID = request.GET.get("sellerID", "")
		subOrderID = request.GET.get("suborderID", "")
		accessToken = request.GET.get("access_token", "")

		tokenPayload = get_token_payload(accessToken, "sellerID")
		subOrderParameters["isSeller"] = 0
		if "sellerID" in tokenPayload and tokenPayload["sellerID"]!=None:
			subOrderParameters["sellersArr"] = [tokenPayload["sellerID"]]
			subOrderParameters["isSeller"] = 1
		else:
			subOrderParameters["sellersArr"] = [int(e) if e.isdigit() else e for e in sellerID.split(",")]

		tokenPayload = get_token_payload(accessToken, "internaluserID")
		subOrderParameters["isInternalUser"] = 0
		subOrderParameters["internalusersArr"] = []
		if "internaluserID" in tokenPayload and tokenPayload["internaluserID"]!=None:
			subOrderParameters["internalusersArr"] = [tokenPayload["internaluserID"]]
			subOrderParameters["isInternalUser"] = 1

		if status != "":
			subOrderParameters["statusArr"] = [int(e) if e.isdigit() else e for e in status.split(",")]

		if subOrderID != "":
			subOrderParameters["subOrderArr"] = [int(e) if e.isdigit() else e for e in subOrderID.split(",")]

		if subOrderParameters["isSeller"] == 0 and subOrderParameters["isInternalUser"] == 0:
			return customResponse("4XX", {"error": "Authentication failure"})

		return order.get_suborder_details(request,subOrderParameters)
	elif request.method == "PUT":
		return order.update_suborder(request)

	return customResponse("4XX", {"error": "Invalid request"})

@csrf_exempt
def order_details(request):

	if request.method == "GET":
		status = request.GET.get("status", "")
		buyerID = request.GET.get("buyerID", "")

		accessToken = request.GET.get("access_token", "")
		tokenPayload = get_token_payload(accessToken, "buyerID")
		isBuyer = 0
		if "buyerID" in tokenPayload and tokenPayload["buyerID"]!=None:
			buyerssArr = [tokenPayload["buyerID"]]
			isBuyer = 1
		elif buyerID == "":
			buyerssArr = []
		else:
			buyerssArr = [int(e) if e.isdigit() else e for e in buyerID.split(",")]

		tokenPayload = get_token_payload(accessToken, "internaluserID")
		isInternalUser = 0
		internalusersArr = []
		if "internaluserID" in tokenPayload and tokenPayload["internaluserID"]!=None:
			internalusersArr = [tokenPayload["internaluserID"]]
			isInternalUser = 1

		if status == "":
			statusArr = []
		else:
			statusArr = [int(e) if e.isdigit() else e for e in status.split(",")]

		return order.get_order_details(request,statusArr,buyerssArr, isBuyer,internalusersArr,isInternalUser)
	elif request.method == "POST":
		return order.post_new_order(request)

	return customResponse("4XX", {"error": "Invalid request"})

@csrf_exempt
def order_item_details(request):

	if request.method == "GET":
		status = request.GET.get("status", "")
		sellerID = request.GET.get("sellerID", "")

		accessToken = request.GET.get("access_token", "")
		tokenPayload = get_token_payload(accessToken, "sellerID")
		isSeller = 0
		if "sellerID" in tokenPayload and tokenPayload["sellerID"]!=None:
			sellersArr = [tokenPayload["sellerID"]]
			isSeller = 1
		elif sellerID == "":
			sellersArr = []
		else:
			sellersArr = [int(e) if e.isdigit() else e for e in sellerID.split(",")]

		tokenPayload = get_token_payload(accessToken, "internaluserID")
		isInternalUser = 0
		internalusersArr = []
		if "internaluserID" in tokenPayload and tokenPayload["internaluserID"]!=None:
			internalusersArr = [tokenPayload["internaluserID"]]
			isInternalUser = 1

		if status == "":
			statusArr = []
		else:
			statusArr = [int(e) if e.isdigit() else e for e in status.split(",")]

		return order.get_order_item_details(request,statusArr,sellersArr, isSeller,internalusersArr,isInternalUser)
	elif request.method == "DELETE":
		return order.cancel_order_item(request)

	return customResponse("4XX", {"error": "Invalid request"})

@csrf_exempt
def buyer_payment_details(request):

	if request.method == "GET":
		status = request.GET.get("status", "")
		buyerID = request.GET.get("buyerID", "")

		accessToken = request.GET.get("access_token", "")
		tokenPayload = get_token_payload(accessToken, "buyerID")
		isBuyer = 0
		if "buyerID" in tokenPayload and tokenPayload["buyerID"]!=None:
			buyersArr = [tokenPayload["buyerID"]]
			isBuyer = 1
		elif buyerID == "":
			buyersArr = []
		else:
			buyersArr = [int(e) if e.isdigit() else e for e in buyerID.split(",")]

		tokenPayload = get_token_payload(accessToken, "internaluserID")
		isInternalUser = 0
		internalusersArr = []
		if "internaluserID" in tokenPayload and tokenPayload["internaluserID"]!=None:
			internalusersArr = [tokenPayload["internaluserID"]]
			isInternalUser = 1

		if status == "":
			statusArr = []
		else:
			statusArr = [int(e) if e.isdigit() else e for e in status.split(",")]

		return order.get_buyer_payment_details(request,statusArr,buyersArr, isBuyer,internalusersArr,isInternalUser)
	elif request.method == "POST":
		return order.post_new_buyer_payment(request)


	return customResponse("4XX", {"error": "Invalid request"})

@csrf_exempt
def seller_payment_details(request):

	if request.method == "GET":
		status = request.GET.get("status", "")
		sellerID = request.GET.get("sellerID", "")

		accessToken = request.GET.get("access_token", "")
		tokenPayload = get_token_payload(accessToken, "sellerID")
		isSeller = 0
		if "sellerID" in tokenPayload and tokenPayload["sellerID"]!=None:
			sellersArr = [tokenPayload["sellerID"]]
			isSeller = 1
		elif sellerID == "":
			sellersArr = []
		else:
			sellersArr = [int(e) if e.isdigit() else e for e in sellerID.split(",")]

		tokenPayload = get_token_payload(accessToken, "internaluserID")
		isInternalUser = 0
		internalusersArr = []
		if "internaluserID" in tokenPayload and tokenPayload["internaluserID"]!=None:
			internalusersArr = [tokenPayload["internaluserID"]]
			isInternalUser = 1

		if status == "":
			statusArr = []
		else:
			statusArr = [int(e) if e.isdigit() else e for e in status.split(",")]

		return order.get_seller_payment_details(request,statusArr,sellersArr, isSeller,internalusersArr,isInternalUser)
	elif request.method == "POST":
		return order.post_new_seller_payment(request)

	return customResponse("4XX", {"error": "Invalid request"})