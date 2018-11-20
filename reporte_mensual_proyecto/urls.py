# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('inicio.urls', namespace='inicio')),
    url(r'^usuarios/', include('usuarios.urls', namespace='usuarios')),
    url(r'^sisrep/', include('registro.urls', namespace='registro')),
    url(r'^bitacora/', include('bitacora.urls', namespace='bitacora')),
    url(r'^admin/', include(admin.site.urls)),
]
