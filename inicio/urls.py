# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from usuarios import views
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
	url(r'^$', login_required(Index.as_view()), name='index'),
)
