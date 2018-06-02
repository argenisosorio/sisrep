# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views
from registro.views import *
import registro.views as views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^index$', login_required(Index.as_view()), name='index'),
    ##### Crud de los reportes ######
    url(r'^consultar_reporte$', login_required(views.Consultar_reporte.as_view()), name='consultar_reporte'),
    url(r'^registrar_reporte$', login_required(views.Registrar_reporte.as_view()), name='registrar_reporte'),
    url(r'^editar_reporte/(?P<pk>\d+)$', login_required(views.Editar_reporte.as_view()), name='editar_reporte'),
    url(r'^borrar_reporte/(?P<pk>\d+)$', login_required(views.Borrar_reporte.as_view()), name='borrar_reporte'),
    url(r'^detallar_reporte/(?P<pk>\d+)$', login_required(views.Detallar_reporte.as_view()), name='detallar_reporte'),
    ##### Filtros de búsqueda #####
    url(r'^buscar/$', login_required(views.Buscar_reporte.as_view()), name='buscar'),
    url(r'^busqueda/$', busqueda, name='busqueda'),
)
