# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from safet import views
from safet.views import *
import safet.views as views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    ##### Crud de los proyectos poa ######
    url(r'^consultar_proyecto$', login_required(views.Consultar_proyecto.as_view()), name='consultar_proyecto'),
    url(r'^registrar_proyecto$', login_required(views.Registrar_proyecto.as_view()), name='registrar_proyecto'),
    url(r'^editar_proyecto/(?P<pk>\d+)$', login_required(views.Editar_proyecto.as_view()), name='editar_proyecto'),
    url(r'^borrar_proyecto/(?P<pk>\d+)$', login_required(views.Borrar_proyecto.as_view()), name='borrar_proyecto'),
    ##### Crud de las acciones específicas ######
    url(r'^consultar_accion$', login_required(views.Consultar_accion.as_view()), name='consultar_accion'),
    url(r'^registrar_accion$', login_required(views.Registrar_accion.as_view()), name='registrar_accion'),
    url(r'^editar_accion/(?P<pk>\d+)$', login_required(views.Editar_accion.as_view()), name='editar_accion'),
    url(r'^borrar_accion/(?P<pk>\d+)$', login_required(views.Borrar_accion.as_view()), name='borrar_accion'),
    ##### Crud de los Reportes de Avances para los analistas ######
    url(r'^consultar_reporte_avances$', login_required(views.Consultar_reporte_avances.as_view()), name='consultar_reporte_avances'),
    url(r'^registrar_reporte_avances$', login_required(views.Registrar_reporte_avances.as_view()), name='registrar_reporte_avances'),
    url(r'^editar_reporte_avances/(?P<pk>\d+)$', login_required(views.Editar_reporte_avances.as_view()), name='editar_reporte_avances'),
    url(r'^detallar_reporte_avances/(?P<pk>\d+)$', login_required(views.Detallar_reporte_avances.as_view()), name='detallar_reporte_avances'),
    url(r'^registrar_reporte_avances_software$', login_required(views.Registrar_reporte_avances_software.as_view()), name='registrar_reporte_avances_software'),
    url(r'^registrar_reporte_avances_cur_lin$', login_required(views.Registrar_reporte_avances_cur_lin.as_view()), name='registrar_reporte_avances_cur_lin'),
    url(r'^registrar_reporte_avances_jornada$', login_required(views.Registrar_reporte_avances_jornada.as_view()), name='registrar_reporte_avances_jornada'),
    ##### Crud de los Reportes de Avances para los CV ######
    url(r'^consultar_reporte_avances_cv$', login_required(views.Consultar_reporte_avances_cv.as_view()), name='consultar_reporte_avances_cv'),
    url(r'^editar_reporte_avances_cv/(?P<pk>\d+)$', login_required(views.Editar_reporte_avances_cv.as_view()), name='editar_reporte_avances_cv'),
    ##### Reportes porcentuales #####
    url(r'^buscar/$', login_required(views.Buscar.as_view()), name='consultar_reporte_avances_cv_por'),
    url(r'^busqueda/$', login_required(views.busqueda), name='busqueda'),
)
