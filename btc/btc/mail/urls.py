
from django.conf.urls.defaults import *
from mail.models import *
from mail.views import *

urlpatterns = patterns('',
    (r'^$', addToMail),
)
