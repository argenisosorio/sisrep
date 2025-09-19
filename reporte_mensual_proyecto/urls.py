# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import JsonResponse


urlpatterns = [
    url(r'^', include('inicio.urls', namespace='inicio')),
    url(r'^usuarios/', include('usuarios.urls', namespace='usuarios')),
    url(r'^sisrep/', include('registro.urls', namespace='registro')),
    url(r'^safet/', include('safet.urls', namespace='safet')),
    url(r'^bitacora/', include('bitacora.urls', namespace='bitacora')),
    url(r'^admin/', include(admin.site.urls)),
    # Devolver la versión del software.
    url(r'^version/$',
        lambda request: JsonResponse({
            'version': open(os.path.join(settings.BASE_DIR, 'VERSION.txt')).read().strip()
        }),
        name='version'),
]
