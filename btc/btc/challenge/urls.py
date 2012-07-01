from django.conf.urls.defaults import *
from challenge.models import *
from challenge.views import *

urlpatterns = patterns('',
  #  (r'^day/(?P<cid>[^/]+)/$', daily_challenge_display),
    (r'^day/(?P<year>[^/]+)/(?P<month>[^/]+)/(?P<day>[^/]+)/$', dated_challenge_display),
    (r'^day/previous/(?P<year>[^/]+)/(?P<month>[^/]+)/(?P<day>[^/]+)/$', previous_day),
    (r'^day/next/(?P<year>[^/]+)/(?P<month>[^/]+)/(?P<day>[^/]+)/$', next_day),
    (r'^$', today_challenge_display),
)
