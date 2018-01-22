from django.conf.urls import url
from author.views import *

urlpatterns = [
    url(r'^$', Authors,name='authors'),
    url(r'^detail/(?P<id>\d+)/$',detail,name='detail'),
]