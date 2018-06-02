# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('usuarios.urls', namespace='usuarios')),
    url(r'^', include('registro.urls', namespace='registro')),
    url(r'^admin/', include(admin.site.urls)),
]
