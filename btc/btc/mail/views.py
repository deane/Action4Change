from challenge.models import *
from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.template import Context, loader
from django.shortcuts import redirect

from challenge.models import *
import datetime

def addToMail(request):
    mail = request.GET.get('mail', None)
    if mail:
        rem = reminder.objects.create(rem_address=mail)
        rem.save()
    #todo: give a javascript answer to pop up
    html = '<html><body>You subscribe for the Daily Reminder a reminder.</body></html>'
    return HttpResponse(html)
