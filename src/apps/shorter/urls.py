from django.conf.urls import url
from apps.shorter.views import IndexView, UrlShorterRedirect

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<url_short>[\w-]+)/$', UrlShorterRedirect.as_view(), name='url_short'),
]
