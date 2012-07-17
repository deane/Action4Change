from django.core.management.base import BaseCommand, CommandError
import datetime

class Command(BaseCommand):
    help = 'Sends daily emails'
    
    def handle(self, *args, **options):
        d = datetime.datetime.now()
        print("cron is working at "+d.isoformat(' '))


