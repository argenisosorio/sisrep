# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from safet import views
from safet.views import *
import safet.views as views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    ##### Crud de los Proyectos POA ######
    url(r'^consultar_proyecto$', login_required(views.Consultar_proyecto.as_view()), name='consultar_proyecto'),
    url(r'^registrar_proyecto$', login_required(views.Registrar_proyecto.as_view()), name='registrar_proyecto'),
    url(r'^editar_proyecto/(?P<pk>\d+)$', login_required(views.Editar_proyecto.as_view()), name='editar_proyecto'),
    url(r'^borrar_proyecto/(?P<pk>\d+)$', login_required(views.Borrar_proyecto.as_view()), name='borrar_proyecto'),
    ##### Crud de las Acciones Específicas ######
    url(r'^consultar_accion$', login_required(views.Consultar_accion.as_view()), name='consultar_accion'),
    url(r'^registrar_accion$', login_required(views.Registrar_accion.as_view()), name='registrar_accion'),
    url(r'^editar_accion/(?P<pk>\d+)$', login_required(views.Editar_accion.as_view()), name='editar_accion'),
    url(r'^borrar_accion/(?P<pk>\d+)$', login_required(views.Borrar_accion.as_view()), name='borrar_accion'),
)
