# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from reportes import views
from reportes.views import *
import reportes.views as views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
	##### Crud de los indicadores ######
    url(r'^inicio$', login_required(IndexReportes.as_view()), name='reportes_inicio'),
    url(r'^consultar_indicadores$', login_required(views.Consultar_indicadores.as_view()), name='consultar_indicadores'),
    url(r'^registrar_indicador$', login_required(views.Registrar_indicadores.as_view()), name='registrar_indicador'),
    url(r'^editar_indicador/(?P<pk>\d+)$', login_required(views.Editar_indicadores.as_view()), name='editar_indicador'),
    url(r'^detallar_indicador/(?P<pk>\d+)$', login_required(views.Detallar_indicadores.as_view()), name='detallar_indicador'),
    url(r'^borrar_indicador/(?P<pk>\d+)$',login_required(views.Borrar_indicadores.as_view()),name='borrar_indicador'),
)
