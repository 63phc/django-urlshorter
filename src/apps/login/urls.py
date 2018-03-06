from django.conf.urls import url, include
from django.contrib import admin

from apps.login import views

urlpatterns = [
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]



