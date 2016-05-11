from django.db import models
from scripts.utils import validate_date_time

#Make changes in model, validate, populate and serializer 

class Seller(models.Model):
    name = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    mobile_number = models.CharField(max_length=11, blank=False, db_index=True)
    email = models.EmailField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    alternate_phone_number = models.CharField(max_length=11, blank=True)
    mobile_verification = models.BooleanField(default=False)
    email_verification = models.BooleanField(default=False)
    company_profile = models.TextField(blank=True)
    seller_conditions = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    delete_status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class SellerAddress(models.Model):
    seller = models.ForeignKey(Seller)

    address = models.CharField(max_length=255, blank=True, null=False)
    landmark = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True, default="India")
    contact_number = models.CharField(max_length=11, blank=True)
    pincode = models.CharField(max_length=6, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.seller.name

class SellerDetails(models.Model):

    seller = models.OneToOneField(Seller)

    vat_tin = models.CharField(max_length=20, blank=True)
    cst = models.CharField(max_length=20, blank=True)

    pan = models.CharField(max_length=10, blank=True, null=False)
    name_on_pan = models.CharField(max_length=100, blank=True, null=False)
    dob_on_pan = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    pan_verification = models.BooleanField(default=0, blank=False, null=False)
    tin_verification = models.BooleanField(default=0, blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.seller.name

class SellerBankDetails(models.Model):

    seller = models.ForeignKey(Seller)

    account_holders_name = models.CharField(max_length=100, blank=True)
    account_number = models.CharField(max_length=18, blank=True)
    ifsc = models.CharField(max_length=11, blank=True)
    bank_name = models.CharField(max_length=50, blank=True)

    branch  = models.CharField(max_length=200, blank=True)
    branch_city = models.CharField(max_length=50, blank=True)
    branch_pincode = models.CharField(max_length=6, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.seller.name

def validateSellerData(seller, oldseller, isnew):

    flag = 0

    if not "name" in seller or not seller["name"]!=None:
        flag = 1
        seller["name"] = oldseller.name
    if not "company_name" in seller or not seller["company_name"]!=None:
        seller["company_name"] = oldseller.company_name
    if not "mobile_number" in seller or not seller["mobile_number"]!=None:
        flag = 1
        seller["mobile_number"] = oldseller.mobile_number
    if not "email" in seller or not seller["email"]!=None:
        seller["email"] = oldseller.email
    if not "password" in seller or not seller["password"]!=None:
        seller["password"] = oldseller.password
    if not "alternate_phone_number" in seller or not seller["alternate_phone_number"]!=None:
        seller["alternate_phone_number"] = oldseller.alternate_phone_number
    if not "mobile_verification" in seller or not seller["mobile_verification"]!=None:
        seller["mobile_verification"] = oldseller.mobile_verification
    if not "email_verification" in seller or not seller["email_verification"]!=None:
        seller["email_verification"] = oldseller.email_verification
    if not "company_profile" in seller or not seller["company_profile"]!=None:
        seller["company_profile"] = oldseller.company_profile
    if not "seller_conditions" in seller or not seller["seller_conditions"]!=None:
        seller["seller_conditions"] = oldseller.seller_conditions

    if isnew == 1 and flag == 1:
        return False

    return True

def validateSellerAddressData(selleraddress, oldselleraddress):

    if not "address" in selleraddress or not selleraddress["address"]!=None:
        selleraddress["address"] = oldselleraddress.address
    if not "landmark" in selleraddress or not selleraddress["landmark"]!=None:
        selleraddress["landmark"] = oldselleraddress.landmark
    if not "city" in selleraddress or not selleraddress["city"]!=None:
        selleraddress["city"] = oldselleraddress.city
    if not "state" in selleraddress or not selleraddress["state"]!=None:
        selleraddress["state"] = oldselleraddress.state
    if not "country" in selleraddress or not selleraddress["country"]!=None:
        selleraddress["country"] = oldselleraddress.country
    if not "contact_number" in selleraddress or not selleraddress["contact_number"]!=None:
        selleraddress["contact_number"] = oldselleraddress.contact_number
    if not "pincode" in selleraddress or not selleraddress["pincode"]!=None:
        selleraddress["pincode"] = oldselleraddress.pincode

def validateSellerDetailsData(sellerdetails, oldsellerdetails):
    if not "vat_tin" in sellerdetails or not sellerdetails["vat_tin"]!=None:
        sellerdetails["vat_tin"] = oldsellerdetails.vat_tin
    if not "cst" in sellerdetails or not sellerdetails["cst"]!=None:
        sellerdetails["cst"] = oldsellerdetails.cst
    if not "pan" in sellerdetails or not sellerdetails["pan"]!=None:
        sellerdetails["pan"] = oldsellerdetails.pan
    if not "name_on_pan" in sellerdetails or not sellerdetails["name_on_pan"]!=None:
        sellerdetails["name_on_pan"] = oldsellerdetails.name_on_pan
    if not "dob_on_pan" in sellerdetails or not sellerdetails["dob_on_pan"]!=None or not validate_date_time(sellerdetails["dob_on_pan"]):
        sellerdetails["dob_on_pan"] = oldsellerdetails.dob_on_pan
    if not "pan_verification" in sellerdetails or not sellerdetails["pan_verification"]!=None:
        sellerdetails["pan_verification"] = oldsellerdetails.pan_verification
    if not "tin_verification" in sellerdetails or not sellerdetails["tin_verification"]!=None:
        sellerdetails["tin_verification"] = oldsellerdetails.tin_verification

def validateSellerBankdetailsData(sellerbankdetails, oldsellerbankdetails):

    if not "account_holders_name" in sellerbankdetails or not sellerbankdetails["account_holders_name"]!=None:
        sellerbankdetails["account_holders_name"] = oldsellerbankdetails.account_holders_name
    if not "account_number" in sellerbankdetails or not sellerbankdetails["account_number"]!=None:
        sellerbankdetails["account_number"] = oldsellerbankdetails.account_number
    if not "ifsc" in sellerbankdetails or not sellerbankdetails["ifsc"]!=None:
        sellerbankdetails["ifsc"] = oldsellerbankdetails.ifsc
    if not "bank_name" in sellerbankdetails or not sellerbankdetails["bank_name"]!=None:
        sellerbankdetails["bank_name"] = oldsellerbankdetails.bank_name
    if not "branch" in sellerbankdetails or not sellerbankdetails["branch"]!=None:
        sellerbankdetails["branch"] = oldsellerbankdetails.branch
    if not "branch_city" in sellerbankdetails or not sellerbankdetails["branch_city"]!=None:
        sellerbankdetails["branch_city"] = oldsellerbankdetails.branch_city
    if not "branch_pincode" in sellerbankdetails or not sellerbankdetails["branch_pincode"]!=None:
        sellerbankdetails["branch_pincode"] = oldsellerbankdetails.branch_pincode 

def populateSellerData(sellerPtr, seller):
    sellerPtr.name = seller["name"]
    sellerPtr.company_name = seller["company_name"]
    sellerPtr.mobile_number = seller["mobile_number"]
    sellerPtr.email = seller["email"]
    sellerPtr.password = seller["password"]
    sellerPtr.alternate_phone_number = seller["alternate_phone_number"]
    sellerPtr.mobile_verification = bool(seller["mobile_verification"])
    sellerPtr.email_verification = bool(seller["email_verification"])
    sellerPtr.company_profile = seller["company_profile"]
    sellerPtr.seller_conditions = seller["seller_conditions"]

def populateSellerDetailsData(sellerDetailsPtr,sellerdetails):
    sellerDetailsPtr.cst = sellerdetails["cst"]
    sellerDetailsPtr.pan = sellerdetails["pan"]
    sellerDetailsPtr.name_on_pan = sellerdetails["name_on_pan"]
    sellerDetailsPtr.dob_on_pan = sellerdetails["dob_on_pan"]
    sellerDetailsPtr.pan_verification = bool(sellerdetails["pan_verification"])
    sellerDetailsPtr.tin_verification = bool(sellerdetails["tin_verification"])
    sellerDetailsPtr.vat_tin = sellerdetails["vat_tin"]

def populateSellerAddressData(sellerAddressPtr, selleraddress):
    sellerAddressPtr.address = selleraddress["address"]
    sellerAddressPtr.landmark = selleraddress["landmark"]
    sellerAddressPtr.city = selleraddress["city"]
    sellerAddressPtr.state = selleraddress["state"]
    sellerAddressPtr.country = selleraddress["country"]
    sellerAddressPtr.contact_number = selleraddress["contact_number"]
    sellerAddressPtr.pincode = selleraddress["pincode"]

def populateSellerBankDetailsData(sellerBankDetailsPtr,sellerbankdetails):
    sellerBankDetailsPtr.account_holders_name = sellerbankdetails["account_holders_name"]
    sellerBankDetailsPtr.account_number = sellerbankdetails["account_number"]
    sellerBankDetailsPtr.ifsc = sellerbankdetails["ifsc"]
    sellerBankDetailsPtr.bank_name = sellerbankdetails["bank_name"]
    sellerBankDetailsPtr.branch = sellerbankdetails["branch"]
    sellerBankDetailsPtr.branch_city = sellerbankdetails["branch_city"]
    sellerBankDetailsPtr.branch_pincode = sellerbankdetails["branch_pincode"]

def sellerEmailExists(email):
    sellerPtr = Seller.objects.filter(email=email)

    if len(sellerPtr) > 0:
        return True

    return False

def sellerMobileNumberExists(mobileNumber):
    sellerPtr = Seller.objects.filter(mobile_number=mobileNumber)

    if len(sellerPtr) > 0:
        return True

    return False