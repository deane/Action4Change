from django.core.management.base import BaseCommand, CommandError
from challenge.models import *
import urllib2

class Command(BaseCommand):
    help = 'Sends daily emails'
    
    def handle(self, *args, **options):
    #send daily
        tdate = datetime.date.today()
        today = dated_challenge.objects.filter(date=tdate)[0].challenge_id
    
        if today:
            FROM = urllib2.quote('noreply@challenges4change.org')
            SUBJECT = urllib2.quote('Today\'s Daily Challenge Theme: '+ today.theme)
            def MESSAGE(tdate, today, email):
                return urllib2.quote('\
<a href="http://challenges4change.org/day/'+str(tdate.year)+'/'+str(tdate.month)+'/'+str(tdate.day)+'">View the Daily Challenge online</a>\
<br><br><br>\
Today\'s Theme: '+today.theme+'<br><br>\
'+today.quote+'<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-'+today.attribution+'<br><br>\
'+today.challenge+'<br><br><br><br><br>\
Daily Challenges are brought to you by <a href="http://challengeday.org">Challenge Day</a> and the Be The Change Movement<br><br><br><br><br>\
To unsubscribe from these emails <a href="http://challenges4change.org/mail/un/?mail='+email+'">click here</a>\
            ') 
        print('parsing done')
        rems = reminder.objects.filter(rem_freq="daily", rem_vector="mail")
        #rems = reminder.objects.filter(rem_address="dedean333@hotmail.com")
        for r in rems:
            print('sending to : '+r.rem_address)
            mail = urllib2.quote(r.rem_address)
            req = urllib2.Request('\
http://sendgrid.com/api/mail.send.json?to='+mail+'&from='+FROM+'&fromname=Challenges4Change&subject='+SUBJECT+'&html='+MESSAGE(tdate, today, mail)+'&api_user=dean&api_key=dean1')
            response = urllib2.urlopen(req)
            feedback = response.read()
            print(feedback)


