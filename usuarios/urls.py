# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from usuarios import views
from .views import *


urlpatterns = patterns('',
    url(r'^$', LoginView.as_view(), name = "login"),
    url(r'logout/$', views.Logout.as_view(), name='logout'),
)
