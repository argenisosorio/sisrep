# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from registro.models import Bien
from forms import BienForm
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
##### Crud de los Bienes #####
##############################

class Consultar_bien(ListView):
    """
    Clase que permite consultar la lista de bienes registrados.
    """
    model = Bien


class Registrar_bien(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar un bien en el sistema.
    """
    model = Bien
    form_class = BienForm
    success_url = reverse_lazy('registro:consultar_bien')
    success_message = "Se registro el bien con éxito"


class Editar_bien(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de un bien.
    """
    model = Bien
    form_class = BienForm
    success_url = reverse_lazy('registro:consultar_bien')
    success_message = "Se actualizo el bien con éxito"


class Borrar_bien(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar un bien registrado en el sistema.
    """
    model = Bien
    success_url = reverse_lazy('registro:consultar_bien')
    success_message = "Se elimino el bien con éxito"

    def delete(self, request, *args, **kwargs):
        """
        Función que permite mandar un mensaje al
        template cuando se borra un bien.
        """
        messages.success(self.request, self.success_message)
        return super(Borrar_bien, self).delete(request, *args, **kwargs)
