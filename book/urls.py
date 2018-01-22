from django.conf.urls import url
from book.views import *

urlpatterns = [
    url(r'^detail/(\d+)/$',detail,name="detail"),
    url(r'^$',book_book,name='books')
]