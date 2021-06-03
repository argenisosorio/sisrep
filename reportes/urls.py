# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from reportes import views
from reportes.views import *
import reportes.views as views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^reportes_inicio$', login_required(IndexReportes.as_view()), name='reportes_inicio'),
    url(r'^consultar_indicadores$', login_required(views.Consultar_indicadores.as_view()), name='consultar_indicadores'),
    url(r'^registrar_indicadores$', login_required(views.Registrar_indicadores.as_view()), name='registrar_indicadores'),
    url(r'^editar_indicadores/(?P<pk>\d+)$', login_required(views.Editar_indicadores.as_view()), name='editar_indicadores'),
    url(r'^detallar_indicadores/(?P<pk>\d+)$', login_required(views.Detallar_indicadores.as_view()), name='detallar_indicadores'),
    url(r'^borrar_indicadores/(?P<pk>\d+)$',login_required(views.Borrar_indicadores.as_view()),name='borrar_indicadores'),
)
