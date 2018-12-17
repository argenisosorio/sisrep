# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from safet.models import ProyectoPoa, AccionEspecifica, ReporteAvances
from bitacora.models import Bitacora
from forms import ProyectoPoaForm, AccionEspecificaForm, ReporteAvancesForm, ReporteAvancesSoftwareForm, ReporteAvancesCursoLineaForm, ReporteAvancesJornadaForm, ReporteAvancesCVForm
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

#####################################
##### Crud de los Proyectos POA #####
#####################################

class Consultar_proyecto(ListView):
    """
    Clase que permite consultar la lista de Proyectos.
    """
    model = ProyectoPoa

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
            messages_alert = ['No tiene permisos para listar los Proyectos POA']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Registrar_proyecto(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar un Proyecto en el sistema.
    """
    model = ProyectoPoa
    form_class = ProyectoPoaForm
    success_url = reverse_lazy('safet:consultar_proyecto')
    success_message = "Se registro el Proyecto POA con éxito"

    def get(self, request, *args, **kwargs):
        """
        Méroto que valida si el usuario autenticado es admin
        para poder registrar un proyecto.
        """
        self.object = None
        if request.user.is_superuser:
            return super(Registrar_proyecto, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar un Proyecto POA']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Editar_proyecto(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de un Proyecto.
    """
    model = ProyectoPoa
    form_class = ProyectoPoaForm
    success_url = reverse_lazy('safet:consultar_proyecto')
    success_message = "Se actualizo el Proyecto POA con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar el proyecto no es admin.
        """
        self.object = self.get_object()
        if request.user.is_superuser:
            return super(Editar_proyecto, self).get(request, *args, **kwargs)
        else:
            if str(self.object) == str(self.request.user):
                return super(Editar_proyecto, self).get(request, *args, **kwargs)
            else:
                messages_alert = ['No tiene permisos para editar el Proyecto POA']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Borrar_proyecto(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar un reporte registrado en el sistema.
    """
    model = ProyectoPoa
    success_url = reverse_lazy('safet:consultar_proyecto')
    success_message = "Se elimino el Proyecto POA con éxito"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Borrar_proyecto, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta borrar el proyecto no es admin.
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
                messages_alert = ['No tiene permisos para borrar el Proyecto POA']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))

######################################################
##### Crud de las Acciones Específicas Proyectos #####
######################################################

class Consultar_accion(ListView):
    """
    Clase que permite consultar la lista de Acciones Específicas.
    """
    model = AccionEspecifica

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
            messages_alert = ['No tiene permisos para listar las Acciones Específicas']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Registrar_accion(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar una Acción Específica.
    """
    model = AccionEspecifica
    form_class = AccionEspecificaForm
    success_url = reverse_lazy('safet:consultar_accion')
    success_message = "Se registro la Acción Específica con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que valida si el usuario autenticado es admin
        para poder registrar una Acción Específica.
        """
        self.object = None
        if request.user.is_superuser:
            return super(Registrar_accion, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar una Acción Específica']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Editar_accion(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de una Acción Específica.
    """
    model = AccionEspecifica
    form_class = AccionEspecificaForm
    success_url = reverse_lazy('safet:consultar_accion')
    success_message = "Se actualizo la Acción Específica con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar la Acción Específica no es admin.
        """
        self.object = self.get_object()
        if request.user.is_superuser:
            return super(Editar_accion, self).get(request, *args, **kwargs)
        else:
            if str(self.object) == str(self.request.user):
                return super(Editar_accion, self).get(request, *args, **kwargs)
            else:
                messages_alert = ['No tiene permisos para editar la Acción Específica']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Borrar_accion(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar una Acción Específica registrada en el sistema.
    """
    model = AccionEspecifica
    success_url = reverse_lazy('safet:consultar_accion')
    success_message = "Se elimino la Acción Específica con éxito"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Borrar_accion, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta borrar una Acción Específica no es admin.
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
                messages_alert = ['No tiene permisos para borrar la Acción Específica']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))

##############################################################
##### Crud de los Reportes de Avances para los Analistas #####
##############################################################

class Consultar_reporte_avances(ListView):
    """
    Clase que permite listar los Reportes de Avances.
    """
    model = ReporteAvances


class Registrar_reporte_avances(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar un Reporte de Avances.
    """
    model = ReporteAvances
    form_class = ReporteAvancesForm
    success_url = reverse_lazy('safet:consultar_reporte_avances')

    def get(self, request, *args, **kwargs):
        """
        Método que valida si el usuario autenticado es admin
        para poder registrar un Reporte de Avances.
        """
        self.object = None
        if request.user.is_superuser:
            return super(Registrar_reporte_avances, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar un Reporte de Avances']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Registrar_reporte_avances_software(CreateView):
    """
    Clase que permite registrar un Reporte de Avances de un producto
    del tipo Software.
    """
    model = ReporteAvances
    form_class = ReporteAvancesSoftwareForm
    template_name = "safet/reporteavances_software_form.html"
    success_url = reverse_lazy('safet:consultar_reporte_avances')

    def get(self, request, *args, **kwargs):
        """
        Método que valida si el usuario autenticado es admin
        para poder registrar un Reporte de Avances.
        """
        self.object = None
        if request.user.is_superuser:
            return super(Registrar_reporte_avances_software, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar un Reporte de Avances']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Registrar_reporte_avances_cur_lin(CreateView):
    """
    Clase que permite registrar un Reporte de Avances de un producto
    del tipo Curso en Línea.
    """
    model = ReporteAvances
    form_class = ReporteAvancesCursoLineaForm
    template_name = "safet/reporteavances_cur_lin_form.html"
    success_url = reverse_lazy('safet:consultar_reporte_avances')

    def get(self, request, *args, **kwargs):
        """
        Método que valida si el usuario autenticado es admin
        para poder registrar un Reporte de Avances.
        """
        self.object = None
        if request.user.is_superuser:
            return super(Registrar_reporte_avances_cur_lin, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar un Reporte de Avances']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Registrar_reporte_avances_jornada(CreateView):
    """
    Clase que permite registrar un Reporte de Avances de un producto
    del tipo Jornada.
    """
    model = ReporteAvances
    form_class = ReporteAvancesJornadaForm
    template_name = "safet/reporteavances_jornada_form.html"
    success_url = reverse_lazy('safet:consultar_reporte_avances')

    def get(self, request, *args, **kwargs):
        """
        Método que valida si el usuario autenticado es admin
        para poder registrar un Reporte de Avances.
        """
        self.object = None
        if request.user.is_superuser:
            return super(Registrar_reporte_avances_jornada, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar un Reporte de Avances']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Editar_reporte_avances(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar los datos de un Reporte de Avances.
    """
    model = ReporteAvances
    form_class = ReporteAvancesForm
    success_url = reverse_lazy('safet:consultar_reporte_avances')

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar el proyecto no es admin.
        """
        self.object = self.get_object()
        if request.user.is_superuser:
            return super(Editar_reporte_avances, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para editar el Reporte de Avances']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Detallar_reporte_avances(DetailView):
    """
    Clase que permite detallar los datos de un Reporte de Avances.
    """
    model = ReporteAvances
    template_name = "safet/reporteavances_detail.html"

def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta ver el reporte no es admin.
        """
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if request.user.is_staff:
            return self.render_to_response(context)
        else:
            messages_alert = ['No tiene permisos para ver el reporte de Avances Porcentuales']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


#######################################################
##### Crud de los Reportes de Avances para los CV #####
#######################################################

class Consultar_reporte_avances_cv(ListView):
    """
    Clase que permite listar los Reportes de Avances.
    """
    model = ReporteAvances
    template_name = "safet/reporteavances_list_cv.html"


class Editar_reporte_avances_cv(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar los datos de un Reporte de Avances.
    """
    model = ReporteAvances
    form_class = ReporteAvancesCVForm
    success_url = reverse_lazy('safet:consultar_reporte_avances_cv')
    template_name = "safet/reporteavances_form_cv.html"


    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar el reporte no es el autor/creador.
        """
        self.object = self.get_object()
        if request.user.is_superuser:
            return super(Editar_reporte_avances_cv, self).get(request, *args, **kwargs)
        else:
            if str(self.object) == str(self.request.user):
                return super(Editar_reporte_avances_cv, self).get(request, *args, **kwargs)
            else:
                messages_alert = ['No tiene permisos para editar el reporte']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))