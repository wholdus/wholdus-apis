from django.db import models


class SellerLeads(models.Model):

	company_name = models.CharField(max_length=200, blank=True)
	email = models.EmailField(max_length=255, blank=True)
	mobile_number = models.CharField(max_length=11, blank=True, db_index=True)

	status = models.IntegerField(default=0)
	comments = models.TextField(blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.mobile_number

def validateSellerLeadData(sellerlead, oldsellerlead, is_new):

	flag = 0

	if not "company_name" in sellerlead or sellerlead["company_name"]==None:
		flag = 1
		sellerlead["company_name"] = oldsellerlead.company_name
	if not "mobile_number" in sellerlead or sellerlead["mobile_number"]==None:
		flag = 1
		sellerlead["mobile_number"] = oldsellerlead.mobile_number
	if not "email" in sellerlead or sellerlead["email"]==None:
		sellerlead["email"] = oldsellerlead.email
	if not "status" in sellerlead or sellerlead["status"]==None:
		sellerlead["status"] = oldsellerlead.status
	if not "comments" in sellerlead or sellerlead["comments"]==None:
		sellerlead["comments"] = oldsellerlead.comments

	if is_new == 1 and flag == 1:
		return False

	return True

def populateSellerLead(sellerleadPtr, sellerlead):
	sellerleadPtr.company_name = sellerlead["company_name"]
	sellerleadPtr.email = sellerlead["email"]
	sellerleadPtr.mobile_number = sellerlead["mobile_number"]
	sellerleadPtr.status = int(sellerlead["status"])
	sellerleadPtr.comments = sellerlead["comments"]

SellerLeadStatus = {
	1:"New",
	2:"Resolved"
}