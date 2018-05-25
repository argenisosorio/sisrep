# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from registro.models import Reporte
from forms import ReporteForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import *
from django.core.urlresolvers import *
from django.db.models import Count
from django.template import RequestContext


class Index(TemplateView):
    """
    Plantilla de inicio del sistema
    """
    template_name = "registro/index.html"

##############################
##### Crud de los Reportes #####
##############################

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


class Editar_reporte(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de un reporte.
    """
    model = Reporte
    form_class = ReporteForm
    success_url = reverse_lazy('registro:consultar_reporte')
    success_message = "Se actualizo el reporte con éxito"


class Borrar_reporte(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar un reporte registrado en el sistema.
    """
    model = Reporte
    success_url = reverse_lazy('registro:consultar_reporte')
    success_message = "Se elimino el reporte con éxito"

    def delete(self, request, *args, **kwargs):
        """
        Función que permite mandar un mensaje al
        template cuando se borra un reporte.
        """
        messages.success(self.request, self.success_message)
        return super(Borrar_reporte, self).delete(request, *args, **kwargs)
