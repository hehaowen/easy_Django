from django.conf.urls import url
from publisher.views import *

urlpatterns = [
    url(r'^$',Publisher_def),
    url(r'^Publishers/',Publisher_pub,name='Publishers'),
    url(r'^detail/(\d+)/$', detail, name='detail'),
]