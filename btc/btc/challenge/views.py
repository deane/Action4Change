from challenge.models import *
from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.template import Context, loader
from django.shortcuts import redirect

import datetime
"""
def daily_challenge_display(request, cid=None):
        Display a daily challenge by id
    
    t = loader.get_template('dc.html')
    dc = daily_challenge.objects.get(id=cid)
    template_vars = {'dc': dc, 'request': request, 'MEDIA_URL': settings.MEDIA_URL}
    c = Context(template_vars)
    rendered = t.render(c)
    resp = HttpResponse(rendered)
    return resp

"""
def today_challenge_display(request):
    """
        Display today's challenge
    """
    d = datetime.date.today()
    return redirect('/day/'+str(d.year)+'/'+str(d.month)+'/'+str(d.day))


def previous_day(request, year, month, day):
    """
        Display previous day's challenge
    """
    d = datetime.date(int(year), int(month), int(day)) - datetime.timedelta(days=1)
    return redirect('/day/'+str(d.year)+'/'+str(d.month)+'/'+str(d.day))


def next_day(request, year, month, day):
    """
        Display next day's challenge
    """
    d = datetime.date(int(year), int(month), int(day)) + datetime.timedelta(days=1)
    return redirect('/day/'+str(d.year)+'/'+str(d.month)+'/'+str(d.day))


def dated_challenge_display(request, year, month, day):
    """
        Display challenge for given date
    """
    t = loader.get_template('dc.html')
    
    try:
        d = datetime.date(int(year),int(month),int(day))
    except:
        raise('Bad Date!')
    
    challenge = dated_challenge.objects.filter(date=d)[0].challenge_id
    
    if not challenge:
        d = datetime.date( 2012, int(month),int(day))
        challenge = dated_challenge.objects.filter(date=d)[0].challenge_id
    str_date = d.strftime("%B %d, %Y")
    template_vars = {'dc': challenge, 'date':d, 'str_date':str_date, 'request': request, 'MEDIA_URL': settings.MEDIA_URL}
    c = Context(template_vars)
    rendered = t.render(c)
    resp = HttpResponse(rendered)
    return resp
    
