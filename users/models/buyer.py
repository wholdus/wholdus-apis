from django.db import models

## Whenever making any changes, add fields to models, serializers and validation

class Buyer(models.Model):
    name = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    mobile_number = models.CharField(max_length=11, blank=False, db_index=True)
    email = models.EmailField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    alternate_phone_number = models.CharField(max_length=11, blank=True)
    mobile_verification = models.BooleanField(default=False)
    email_verification = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    delete_status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class BuyerAddress(models.Model):
    buyer = models.ForeignKey(Buyer)

    address = models.CharField(max_length=255, blank=True, null=False)
    landmark = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True, default="India")
    contact_number = models.CharField(max_length=11, blank=True)
    pincode = models.CharField(max_length=6, blank=True)

    def __unicode__(self):
        return self.address

class BuyerDetails(models.Model):
    buyer = models.OneToOneField(Buyer)

    vat_tin = models.CharField(max_length=20, blank=True)
    cst = models.CharField(max_length=20, blank=True)

    buyer_interest = models.TextField(blank = True)
    customer_type = models.CharField(max_length=20, blank=True)
    buying_capacity = models.CharField(max_length=20, blank=True)
    buys_from = models.CharField(max_length=20, blank=True)
    purchasing_states = models.TextField(blank = True)

    def __unicode__(self):
        return self.buyer.name

def validateBuyerData(buyer, oldbuyer, is_new):

    flag = 0

    if not "name" in buyer or not buyer["name"]:
        flag = 1
        buyer["name"] = oldbuyer.name
    if not "company_name" in buyer or not buyer["company_name"]:
        buyer["company_name"] = oldbuyer.company_name
    if not "mobile_number" in buyer or not buyer["mobile_number"]:
        flag = 1
        buyer["mobile_number"] = oldbuyer.mobile_number
    if not "email" in buyer or not buyer["email"]:
        buyer["email"] = oldbuyer.email
    if not "password" in buyer or not buyer["password"]:
        buyer["password"] = oldbuyer.password
    if not "alternate_phone_number" in buyer or not buyer["alternate_phone_number"]:
        buyer["alternate_phone_number"] = oldbuyer.alternate_phone_number
    if not "mobile_verification" in buyer or not buyer["mobile_verification"]:
        buyer["mobile_verification"] = oldbuyer.mobile_verification
    if not "email_verification" in buyer or not buyer["email_verification"]:
        buyer["email_verification"] = oldbuyer.email_verification
    if not "gender" in buyer or not buyer["gender"]:
        buyer["gender"] = oldbuyer.gender

    if is_new == 1 and flag == 1:
        return False

    return True


    
def validateBuyerDetailsData(buyerdetails, oldbuyerdetails):

    if not "vat_tin" in buyerdetails or not buyerdetails["vat_tin"]:
        buyerdetails["vat_tin"] = oldbuyerdetails.vat_tin
    if not "cst" in buyerdetails or not buyerdetails["cst"]:
        buyerdetails["cst"] = oldbuyerdetails.cst
    if not "buyer_interest" in buyerdetails or not buyerdetails["buyer_interest"]:
        buyerdetails["buyer_interest"] = oldbuyerdetails.buyer_interest
    if not "customer_type" in buyerdetails or not buyerdetails["customer_type"]:
        buyerdetails["customer_type"] = oldbuyerdetails.customer_type
    if not "buying_capacity" in buyerdetails or not buyerdetails["buying_capacity"]:
        buyerdetails["buying_capacity"] = oldbuyerdetails.buying_capacity
    if not "buys_from" in buyerdetails or not buyerdetails["buys_from"]:
        buyerdetails["buys_from"] = oldbuyerdetails.buys_from
    if not "purchasing_states" in buyerdetails or not buyerdetails["purchasing_states"]:
        buyerdetails["purchasing_states"] = oldbuyerdetails.purchasing_states 


def validateBuyerAddressData(buyeraddress, oldbuyeraddress):

    if not "address" in buyeraddress or not buyeraddress["address"]:
        buyeraddress["address"] = oldbuyeraddress.address
    if not "landmark" in buyeraddress or not buyeraddress["landmark"]:
        buyeraddress["landmark"] = oldbuyeraddress.landmark
    if not "city" in buyeraddress or not buyeraddress["city"]:
        buyeraddress["city"] = oldbuyeraddress.city
    if not "state" in buyeraddress or not buyeraddress["state"]:
        buyeraddress["state"] = oldbuyeraddress.state
    if not "country" in buyeraddress or not buyeraddress["country"]:
        buyeraddress["country"] = oldbuyeraddress.country
    if not "contact_number" in buyeraddress or not buyeraddress["contact_number"]:
        buyeraddress["contact_number"] = oldbuyeraddress.contact_number
    if not "pincode" in buyeraddress or not buyeraddress["pincode"]:
        buyeraddress["pincode"] = oldbuyeraddress.pincode
