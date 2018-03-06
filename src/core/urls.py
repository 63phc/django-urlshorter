from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.shorter.urls')),
    url(r'^auth/', include('apps.login.urls')),
]
