# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from reportes.models import Indicadores
from forms import IndicadoresForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import *
from django.core.urlresolvers import *
from django.db.models import Count
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import redirect
from datetime import datetime
#is_superuser = Analista
#is_staff = Director
#is_active = Cara visible

##################################
##### Crud de los Indicadores ####
##################################

class IndexReportes(TemplateView):
    """
    Plantilla de inicio del módulo de reportes.
    """
    template_name = "reportes/inicio_reportes.html"


class Consultar_indicadores(ListView):
    """
    Clase que permite consultar los indicadores registrados.
    """
    model = Indicadores

    def get(self, request, *args, **kwargs):
        """
        Método que valida si el usuario es admin para ver la lista de objetos.
        """
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            if (self.get_paginate_by(self.object_list) is not None
                    and hasattr(self.object_list, 'exists')):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
                        % {'class_name': self.__class__.__name__})
        context = self.get_context_data()
        if request.user.is_superuser:
            return self.render_to_response(context)
        else:
            messages_alert = ['No tiene permisos para listar los indicadores']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Registrar_indicador(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar un indicador.
    """
    model = Indicadores
    form_class = IndicadoresForm
    success_url = reverse_lazy('reportes:consultar_indicadores')
    success_message = "Se registro el indicador con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que valida si el usuario autenticado es admin
        para poder registrar un indicador.
        """
        self.object = None
        if request.user.is_superuser:
            return super(Registrar_indicador, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar indicadores']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Editar_indicador(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar los datos de un indicador guardado.
    """
    model = Indicadores
    form_class = IndicadoresForm
    template_name = "reportes/indicadores_update.html"
    success_url = reverse_lazy('reportes:consultar_indicadores')
    success_message = "Se actualizo el indicador con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar el indicador no es admin.
        """
        self.object = self.get_object()
        if request.user.is_superuser:
            return super(Editar_indicador, self).get(request, *args, **kwargs)
        else:
            if str(self.object) == str(self.request.user):
                return super(Editar_indicador, self).get(request, *args, **kwargs)
            else:
                messages_alert = ['No tiene permisos para editar el beneficio']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Detallar_indicador(DetailView):
    """
    Clase que muestra los datos detallados de los indicador guardado.
    """
    model = Indicadores
    template_name = "reportes/modals.html"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta ver el reporte no es el autor/creador o un director o admin.
        """
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if request.user.is_staff:
            return self.render_to_response(context)
        else:
            if str(self.object) == str(self.request.user):
                return self.render_to_response(context)
            else:
                messages_alert = ['No tiene permisos para ver el reporte']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Borrar_indicador(SuccessMessageMixin,DeleteView):
    """
    Clase que permite eliminar un indicador registrado.
    """
    model = Indicadores
    success_url = reverse_lazy('reportes:consultar_indicadores')
    success_message = "Se elimino el indicador con éxito"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Borrar_indicador, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta borrar el beneficio no es admin.
        """
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        self.object = self.get_object()
        if request.user.is_superuser:
            return self.render_to_response(context)
        else:
            if str(self.object) == str(self.request.user):
                return self.render_to_response(context)
            else:
                messages_alert = ['No tiene permisos para borrar el indicador']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))
