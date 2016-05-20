from django.http import JsonResponse
from django.db import connection
import datetime
import jwt as JsonWebToken
import settings
import os

from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

def closeDBConnection():
    connection.close()

def customResponse(statusCode, body):
    response = {}
    response["statusCode"] = statusCode
    response["body"] = body

    return JsonResponse(response)

def convert_keys_to_string(dictionary):
    """Recursively converts dictionary keys to strings."""
    if not isinstance(dictionary, dict):
        return dictionary
    return dict((str(k), convert_keys_to_string(v))
        for k, v in dictionary.items())

def validate_date_time(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        return False

    return True

def check_token_validity(access_token):
    if not access_token:
        ## log the exception into db
        return {}
    try:
        tokenPayload = JsonWebToken.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
    except Exception as ex:
        ## log the exception into db
        return {}

    return tokenPayload


def get_token_payload(access_token, userID):
    tokenPayload = check_token_validity(access_token)

    if not "user" in tokenPayload or not userID in tokenPayload:
        return {}

    return tokenPayload

def create_email(mail_template_file,mail_dict,subject,from_email,to,attachment="",bcc=[]):
    mail_template = get_template(mail_template_file)   
    mail_context = Context(mail_dict)
    html_message = mail_template.render(mail_context)
        
    email = EmailMessage(subject=subject,body=html_message,from_email=from_email,to=to,bcc=bcc)

    if (attachment != "" and os.path.isfile(attachment)):
        email.attach_file(attachment)

    email.content_subtype = "html"
    email.send(fail_silently=True)