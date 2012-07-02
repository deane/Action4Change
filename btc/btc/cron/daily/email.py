from challenge.models import *
from django.core.mail import send_mail

# today's challenge
today = dated_challenge.objects.filter(date=datetime.date.today()).challenge

if today:
    FROM = 'noreply@btcinteract.com'
    SUBJECT = 'test'
    MESSAGE = 'test'
    
    rems = reminder.objects.filer(rem_freq="daily", rem_vector="mail")
    for r in rems:
        send_mail(SUBJECT, MESSAGE, FROM, r.rem_address, fail_silently=False)

