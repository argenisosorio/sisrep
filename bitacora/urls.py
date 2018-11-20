# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from bitacora import views
from bitacora.views import *
import bitacora.views as views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^', login_required(views.Bitacora.as_view()), name='bitacora'),
)
