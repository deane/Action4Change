
from django.conf.urls.defaults import *
from mail.models import *
from mail.views import *

urlpatterns = patterns('',
    (r'un/$', unsubscribe),
    (r'^$', addToMail),
)
