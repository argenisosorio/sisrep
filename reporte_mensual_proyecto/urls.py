# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('usuarios.urls', namespace='usuarios')),
    url(r'^registro/', include('registro.urls', namespace='registro')),
    url(r'^bitacora/', include('bitacora.urls', namespace='bitacora')),
    url(r'^admin/', include(admin.site.urls)),
]
