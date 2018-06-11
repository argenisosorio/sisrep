# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from registro.models import Reporte, Proyecto
from bitacora.models import Bitacora
from forms import ReporteForm, ProyectoForm
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


class Index(TemplateView):
    """
    Plantilla de inicio del sistema
    """
    template_name = "registro/index.html"


#################################
##### Crud de los Proyectos #####
#################################

class Consultar_proyecto(ListView):
    """
    Clase que permite consultar la lista de Proyectos.
    """
    model = Proyecto

    def get(self, request, *args, **kwargs):
        """
        Método que valida si un usuario tiene permisos para ver la lista de proyectos.
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
        if request.user.is_staff:
            return self.render_to_response(context)
        else:
            messages_alert = ['No tiene permisos para editar el reporte']
            return render_to_response("registro/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Registrar_proyecto(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar un Proyecto en el sistema.
    """
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy('registro:consultar_proyecto')
    success_message = "Se registro el proyecto con éxito"


class Editar_proyecto(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de un Proyecto.
    """
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy('registro:consultar_proyecto')
    success_message = "Se actualizo el proyecto con éxito"


class Borrar_proyecto(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar un reporte registrado en el sistema.
    """
    model = Proyecto
    success_url = reverse_lazy('registro:consultar_proyecto')
    success_message = "Se elimino el proyecto con éxito"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Borrar_proyecto, self).delete(request, *args, **kwargs)


################################
##### Crud de los Reportes #####
################################

class Consultar_reporte(ListView):
    """
    Clase que permite consultar la lista de reportes.
    """
    model = Reporte


class Registrar_reporte(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar un reporte en el sistema.
    """
    model = Reporte
    form_class = ReporteForm
    success_url = reverse_lazy('registro:consultar_reporte')
    success_message = "Se registro el reporte con éxito"

    def form_valid(self, form):
        """
        Método que permite guardar un evento en la Bitácora cuando
        se registra un Reporte en el sistema.
        """
        usuario = str(self.request.user)
        accion = "Registro un Reporte"
        myDate = datetime.now()
        formatedDate = myDate.strftime("%d-%m-%Y %H:%M")
        fecha_humana = str(formatedDate)
        Bitacora.objects.create(usuario=usuario, accion=accion, fecha=fecha_humana)
        self.object = form.save()
        return super(Registrar_reporte, self).form_valid(form)


class Editar_reporte(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de un reporte.
    """
    model = Reporte
    form_class = ReporteForm
    success_url = reverse_lazy('registro:consultar_reporte')
    success_message = "Se actualizo el reporte con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a /index si el usuario
        que intenta editar el reporte no es el autor/creador.
        """
        self.object = self.get_object()
        if str(self.object) == str(self.request.user):
            return super(Editar_reporte, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para editar el reporte']
            return render_to_response("registro/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Borrar_reporte(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar un reporte registrado en el sistema.
    """
    model = Reporte
    success_url = reverse_lazy('registro:consultar_reporte')
    success_message = "Se elimino el reporte con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a /index si el usuario
        que intenta borrar el reporte no es el autor/creador.
        """
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        self.object = self.get_object()
        if str(self.object) == str(self.request.user):
            return self.render_to_response(context)
        else:
            messages_alert = ['No tiene permisos para borrar el reporte']
            return render_to_response("registro/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))

    def delete(self, request, *args, **kwargs):
        """
        Función que permite mandar un mensaje al template
        cuando se borra un reporte y registra en la Bitácora que
        se elimino un reporte.
        """
        usuario = str(self.request.user)
        accion = "Elimino un Reporte"
        myDate = datetime.now()
        formatedDate = myDate.strftime("%d-%m-%Y %H:%M")
        fecha_humana = str(formatedDate)
        Bitacora.objects.create(usuario=usuario, accion=accion, fecha=fecha_humana)
        messages.success(self.request, self.success_message)
        return super(Borrar_reporte, self).delete(request, *args, **kwargs)


class Detallar_reporte(DetailView):
    """
    Clase que muestra la lista de entradas de la bitácora
    """
    model = Reporte
    template_name = "registro/reporte_detail.html"

    """
    def get(self, request, *args, **kwargs):
        Método que redirecciona a /index si el usuario
        que intenta ver el reporte no es el autor/creador.
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if str(self.object) == str(self.request.user):
            return self.render_to_response(context)
        else:
            context = {}
            messages_alert = ['No tiene permisos para ver el reporte']
            return render_to_response("registro/index.html",{'context': context, 'messages_alert': messages_alert}, context_instance=RequestContext(request))
    """

###############################
##### Filtros de búsqueda #####
###############################

class Buscar_reporte(TemplateView):
    """
    Plantilla que tiene el formulario para buscar reportes.
    """
    template_name = "registro/buscar.html"


def busqueda(request):
    """
    Función que recibe los parámetros enviados desde el formulario de
    búsqueda de reportes y filtra los reportes con querysets.
    """
    if 'ano' in request.GET and request.GET['ano'] and 'mes' in request.GET and request.GET['mes']:
        ano = request.GET['ano']
        mes = request.GET['mes']
        reportes_ano = Reporte.objects.filter(ano__icontains=ano)
        reportes = reportes_ano.filter(mes__icontains=mes)
        return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
    else:
        return HttpResponse('Por favor introduce un termino de búsqueda.')
