import os
from django.core.management.base import NoArgsCommand
from optparse import make_option

class Command(NoArgsCommand):
    help = "Update permissions for all installed apps."

    requires_model_validation = True

    def handle_noargs(self, **options):
        from django.contrib.auth.management import create_permissions
        from django.db.models import get_apps
        for app in get_apps():
           create_permissions(app, None, 2)