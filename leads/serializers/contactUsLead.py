from ..models.contactUsLead import ContactUsLeadStatus

def serialize_contactus_lead(contactUslead_entry):

	contactUsLead = {
		"contactusleadID" : contactUslead_entry.id,
		"remarks" : contactUslead_entry.remarks,
		"email" : contactUslead_entry.email,
		"mobile_number" : contactUslead_entry.mobile_number,
		"comments" : contactUslead_entry.comments,
		"created_at" : contactUslead_entry.created_at,
		"updated_at" : contactUslead_entry.updated_at
	}

	contactUsLead["status"] = {
		"value": contactUslead_entry.status,
		"display_value":ContactUsLeadStatus[contactUslead_entry.status]["display_value"]
	}

	return contactUsLead

def parseContactUsLeads(contactUsLeadQuerySet):

	contactUsLeads = []

	for contactUsLead in contactUsLeadQuerySet:
		contactUsLeadEntry = serialize_contactus_lead(contactUsLead)
		contactUsLeads.append(contactUsLeadEntry)

	return contactUsLeads