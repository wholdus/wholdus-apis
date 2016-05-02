from django.db import models

class BuyerLeads(models.Model):

	name = models.CharField(max_length=200, blank=True)
	email = models.EmailField(max_length=255, blank=True)
	mobile_number = models.CharField(max_length=11, blank=True, db_index=True)

	status = models.IntegerField(default=0)

	def __unicode__(self):
		return self.mobile_number

def validateBuyerLeadData(buyerlead, oldbuyerlead, is_new):

    flag = 0

    if not "name" in buyerlead or not buyerlead["name"]!=None:
        flag = 1
        buyerlead["name"] = oldbuyerlead.name
    if not "mobile_number" in buyerlead or not buyerlead["mobile_number"]!=None:
        flag = 1
        buyerlead["mobile_number"] = oldbuyerlead.mobile_number
    if not "email" in buyerlead or not buyerlead["email"]!=None:
        buyerlead["email"] = oldbuyerlead.email

    if is_new == 1 and flag == 1:
        return False

    return True

def populateBuyerLead(buyerleadPtr, buyerlead):
    buyerleadPtr.name = buyerlead["name"]
    buyerleadPtr.email = buyerlead["email"]
    buyerleadPtr.mobile_number = buyerlead["mobile_number"]