# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views
from registro.views import *
import registro.views as views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    ##### Crud de los proyectos ######
    url(r'^consultar_proyecto$', login_required(views.Consultar_proyecto.as_view()), name='consultar_proyecto'),
    url(r'^registrar_proyecto$', login_required(views.Registrar_proyecto.as_view()), name='registrar_proyecto'),
    url(r'^editar_proyecto/(?P<pk>\d+)$', login_required(views.Editar_proyecto.as_view()), name='editar_proyecto'),
    url(r'^borrar_proyecto/(?P<pk>\d+)$', login_required(views.Borrar_proyecto.as_view()), name='borrar_proyecto'),
    ##### Crud de los cara visibles ######
    url(r'^consultar_cara_visible$', login_required(views.Consultar_cara_visible.as_view()), name='consultar_cara_visible'),
    url(r'^registrar_cara_visible$', login_required(views.Registrar_cara_visible.as_view()), name='registrar_cara_visible'),
    url(r'^editar_cara_visible/(?P<pk>\d+)$', login_required(views.Editar_cara_visible.as_view()), name='editar_cara_visible'),
    url(r'^borrar_cara_visible/(?P<pk>\d+)$', login_required(views.Borrar_cara_visible.as_view()), name='borrar_cara_visible'),
    ##### Crud de los directores ######
    url(r'^consultar_director$', login_required(views.Consultar_director.as_view()), name='consultar_director'),
    url(r'^registrar_director$', login_required(views.Registrar_director.as_view()), name='registrar_director'),
    url(r'^editar_director/(?P<pk>\d+)$', login_required(views.Editar_director.as_view()), name='editar_director'),
    url(r'^borrar_director/(?P<pk>\d+)$', login_required(views.Borrar_director.as_view()), name='borrar_director'),
    ##### Crud de los cargos ######
    url(r'^consultar_cargo$', login_required(views.Consultar_cargo.as_view()), name='consultar_cargo'),
    url(r'^registrar_cargo$', login_required(views.Registrar_cargo.as_view()), name='registrar_cargo'),
    url(r'^editar_cargo/(?P<pk>\d+)$', login_required(views.Editar_cargo.as_view()), name='editar_cargo'),
    url(r'^borrar_cargo/(?P<pk>\d+)$', login_required(views.Borrar_cargo.as_view()), name='borrar_cargo'),
    ##### Crud de los reportes ######
    url(r'^consultar_reporte$', login_required(views.Consultar_reporte.as_view()), name='consultar_reporte'),
    url(r'^registrar_reporte$', login_required(views.Registrar_reporte.as_view()), name='registrar_reporte'),
    url(r'^editar_reporte/(?P<pk>\d+)$', login_required(views.Editar_reporte.as_view()), name='editar_reporte'),
    url(r'^editar_reporte_analista/(?P<pk>\d+)$', login_required(views.Editar_reporte_analista.as_view()), name='editar_reporte_analista'),
    url(r'^borrar_reporte/(?P<pk>\d+)$', login_required(views.Borrar_reporte.as_view()), name='borrar_reporte'),
    url(r'^detallar_reporte/(?P<pk>\d+)$', login_required(views.Detallar_reporte.as_view()), name='detallar_reporte'),
    ##### Filtros de búsqueda #####
    url(r'^buscar/$', login_required(views.Buscar_reporte.as_view()), name='buscar'),
    url(r'^busqueda/$', login_required(views.busqueda), name='busqueda'),
)
