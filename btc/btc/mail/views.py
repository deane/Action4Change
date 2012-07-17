from challenge.models import *
from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.template import Context, loader
from django.shortcuts import redirect

from challenge.models import *
import datetime

def addToMail(request):
    """
        tries to add the email in the 'mail' get parameter
        to the daily mailing list.
        returns a div (might be shown in a pop up)
    """ 
    mail = request.GET.get('mail', None)
    html = '<div class="alert-box alert" style="text-align:center">We didn\'t get your email address.<br> Please login with facebook</div>'
    if mail and not mail=='undefined':
        existing = reminder.objects.filter(rem_address=mail)
        if existing:
            html = '<div class="alert-box alert" style="text-align:center">Your email ('+mail+') is already subscribed to the Daily Challenge mailing list.</div>'
        else:
            rem = reminder.objects.create(rem_address=mail)
            rem.save()
            html = '<div class="alert-box secondary" style="text-align:center">Your email ('+mail+') has been added to the Daily Challenge mailing list.</div>'
    return HttpResponse(html)

def unsubscribe(request):
    """
        tries to add the email in the 'mail' get parameter
        to the daily mailing list.
        returns a div (might be shown in a pop up)
    """
    mail = request.GET.get('mail', None)
    html = '<div class="alert-box alert" style="text-align:center">We didn\'t get your email address.<br> Please login with facebook.</div>'
    if mail and not mail == 'undefined':
        html = '<div class="alert-box alert" style="text-align:center">Your email ('+mail+') has been unsubcribed from the Daily Challenge mailing list.</div>'
        existing = reminder.objects.filter(rem_address=mail)
        for e in existing:
            e.delete() 
    return HttpResponse(html)

