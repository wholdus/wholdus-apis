from scripts.utils import customResponse, closeDBConnection, convert_keys_to_string, responsePaginationParameters
import json

from ..serializers.pincodeserviceability import *
from ..models.serviceability import *

import logging
log = logging.getLogger("django")

from django.core.paginator import Paginator

def get_pincode_serviceability_details(request,parameters = {}):
	try:
		serviceable_pincodes = filterServiceablePincodes(parameters)

		paginator = Paginator(serviceable_pincodes, parameters["itemsPerPage"])

		try:
			pageItems = paginator.page(parameters["pageNumber"])
		except Exception as e:
			pageItems = []


		body = parseServiceablePincodes(pageItems,parameters)

		response = {"serviceable_pincodes": body}

		response = responsePaginationParameters(response, paginator, parameters)

		closeDBConnection()

		statusCode = "2XX"
		
	except Exception as e:
		log.critical(e)
		statusCode = "4XX"
		body = {"error": "Invalid pincode serviceability"}

	return customResponse(statusCode, response)