# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from registro.models import Reporte, Proyecto, Caravisible, Director, Cargo
from bitacora.models import Bitacora
from forms import ReporteForm, ProyectoForm, CaravisibleForm, DirectorForm, CargoForm
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
#is_staff = Supervisor
#is_active = Cara visible


#################################
##### Crud de los productos #####
#################################

class Consultar_proyecto(ListView):
    """
    Clase que permite consultar la lista de Proyectos.
    """
    model = Proyecto

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
            messages_alert = ['No tiene permisos para listar los productos']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Registrar_proyecto(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar un producto.
    """
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy('registro:consultar_proyecto')
    success_message = "Se registro el producto con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que valida si el usuario autenticado es admin
        para poder registrar un producto.
        """
        self.object = None
        if request.user.is_superuser:
            return super(Registrar_proyecto, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar un producto']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Editar_proyecto(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de un producto.
    """
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy('registro:consultar_proyecto')
    success_message = "Se actualizo el producto con éxito"

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
                messages_alert = ['No tiene permisos para editar el producto']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Borrar_proyecto(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar un producto registrado.
    """
    model = Proyecto
    success_url = reverse_lazy('registro:consultar_proyecto')
    success_message = "Se elimino el producto con éxito"

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
                messages_alert = ['No tiene permisos para borrar el producto']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


######################################
##### Crud de los caras visibles #####
######################################

class Consultar_cara_visible(ListView):
    """
    Clase que permite consultar la lista de caras visibles.
    """
    model = Caravisible

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
            messages_alert = ['No tiene permisos para listar los trabajadores']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Registrar_cara_visible(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar un cara visible en el sistema.
    """
    model = Caravisible
    form_class = CaravisibleForm
    success_url = reverse_lazy('registro:consultar_cara_visible')
    success_message = "Se registro el trabajador con éxito"

    def get(self, request, *args, **kwargs):
        """
        Méroto que valida si el usuario autenticado es admin
        para poder registrar un cara visible.
        """
        self.object = None
        if request.user.is_superuser:
            return super(Registrar_cara_visible, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar un cara visible']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Editar_cara_visible(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de un cara visible.
    """
    model = Caravisible
    form_class = CaravisibleForm
    success_url = reverse_lazy('registro:consultar_cara_visible')
    success_message = "Se actualizo el trabajador con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar el cara visible no es admin.
        """
        self.object = self.get_object()
        if request.user.is_superuser:
            return super(Editar_cara_visible, self).get(request, *args, **kwargs)
        else:
            if str(self.object) == str(self.request.user):
                return super(Editar_cara_visible, self).get(request, *args, **kwargs)
            else:
                messages_alert = ['No tiene permisos para editar el cara visble']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Borrar_cara_visible(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar un cara visible registrado en el sistema.
    """
    model = Caravisible
    success_url = reverse_lazy('registro:consultar_cara_visible')
    success_message = "Se elimino el trabajador con éxito"

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
                messages_alert = ['No tiene permisos para borrar el cara visible']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Borrar_cara_visible, self).delete(request, *args, **kwargs)


##################################
##### Crud de los directores #####
##################################

class Consultar_director(ListView):
    """
    Clase que permite consultar la lista de directores.
    """
    model = Director
    template_name = "registro/director_list.html"

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
            messages_alert = ['No tiene permisos para listar los directores']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Registrar_director(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar un director.
    """
    model = Director
    form_class = DirectorForm
    success_url = reverse_lazy('registro:consultar_director')
    success_message = "Se registro el director con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que valida si el usuario autenticado es admin
        para poder registrar un director.
        """
        self.object = None
        if request.user.is_superuser:
            return super(Registrar_director, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar un director']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Editar_director(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de un director.
    """
    model = Director
    form_class = DirectorForm
    success_url = reverse_lazy('registro:consultar_director')
    success_message = "Se actualizo el director con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar el proyecto no es admin.
        """
        self.object = self.get_object()
        if request.user.is_superuser:
            return super(Editar_director, self).get(request, *args, **kwargs)
        else:
            if str(self.object) == str(self.request.user):
                return super(Editar_director, self).get(request, *args, **kwargs)
            else:
                messages_alert = ['No tiene permisos para editar el director']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Borrar_director(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar un director registrado en el sistema.
    """
    model = Director
    success_url = reverse_lazy('registro:consultar_director')
    success_message = "Se elimino el director con éxito"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Borrar_director, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta borrar el director no es admin.
        """
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        self.object = self.get_object()
        if request.user.is_superuser:
            return self.render_to_response(context)
        else:
            messages_alert = ['No tiene permisos para borrar el director']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


##############################
##### Crud de los cargos #####
##############################

class Consultar_cargo(ListView):
    """
    Clase que permite consultar la lista de cargos.
    """
    model = Cargo
    template_name = "registro/cargo_list.html"

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
            messages_alert = ['No tiene permisos para listar los cargos']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Registrar_cargo(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar un cargo.
    """
    model = Cargo
    form_class = CargoForm
    success_url = reverse_lazy('registro:consultar_cargo')
    success_message = "Se registro el cargo con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que valida si el usuario autenticado es admin
        para poder registrar un cargo.
        """
        self.object = None
        if request.user.is_superuser:
            return super(Registrar_cargo, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar un cargo']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Editar_cargo(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de un cargo.
    """
    model = Cargo
    form_class = CargoForm
    success_url = reverse_lazy('registro:consultar_cargo')
    success_message = "Se actualizo el cargo con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar el cargo no es admin.
        """
        self.object = self.get_object()
        if request.user.is_superuser:
            return super(Editar_cargo, self).get(request, *args, **kwargs)
        else:
            if str(self.object) == str(self.request.user):
                return super(Editar_cargo, self).get(request, *args, **kwargs)
            else:
                messages_alert = ['No tiene permisos para editar el cargo']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Borrar_cargo(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar un cargo registrado en el sistema.
    """
    model = Cargo
    success_url = reverse_lazy('registro:consultar_cargo')
    success_message = "Se elimino el cargo con éxito"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Borrar_cargo, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta borrar el cargo no es admin.
        """
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        self.object = self.get_object()
        if request.user.is_superuser:
            return self.render_to_response(context)
        else:
            messages_alert = ['No tiene permisos para borrar el cargo']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


##########################################
##### Crud de los reportes de tareas #####
##########################################

class Consultar_reporte(ListView):
    """
    Clase que permite consultar la lista de reportes de tareas.
    """
    model = Reporte

    def get_queryset(self):
        """
        Método que permite filtrar los reportes dependiendo del
        tipo de usuario que esté autenticado.
        """
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, six.string_types):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        if self.request.user.is_superuser:
            return queryset
        else:
            if self.request.user.is_staff:
                return queryset
            else:
                queryset = queryset.filter(autor=str(self.request.user))
                queryset = queryset.filter(ano=str(2020))
                return queryset


class Registrar_reporte(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar un reporte de tareas en el sistema.
    """
    model = Reporte
    form_class = ReporteForm
    success_url = reverse_lazy('registro:consultar_reporte')
    success_message = "Se registro el reporte de tareas con éxito"

    def form_valid(self, form):
        """
        Método que permite guardar un evento en la Bitácora cuando
        se registra un reporte de actividades en el sistema.
        """
        self.object = form.save()
        usuario = str(self.request.user)
        nombre_proyecto = self.object.nombre_proyecto
        mes = self.object.mes
        accion = "Registro un reporte de tareas del producto "+nombre_proyecto+" del mes de "+mes
        myDate = datetime.now()
        formatedDate = myDate.strftime("%d-%m-%Y %H:%M")
        fecha_humana = str(formatedDate)
        Bitacora.objects.create(usuario=usuario, accion=accion, fecha=fecha_humana)
        return super(Registrar_reporte, self).form_valid(form)


class Editar_reporte(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de un reporte de tareas.
    """
    model = Reporte
    form_class = ReporteForm
    template_name = "registro/reporte_form_update_cv.html"
    success_url = reverse_lazy('registro:consultar_reporte')
    success_message = "Se actualizo el reporte con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar el reporte no es el autor/creador.
        """
        self.object = self.get_object()
        if request.user.is_superuser:
            return super(Editar_reporte, self).get(request, *args, **kwargs)
        else:
            if str(self.object) == str(self.request.user):
                if str(self.object.estatus) == "act":
                    """
                    Validación del reporte, si está inactivo no tiene permiso de editar.
                    """
                    return super(Editar_reporte, self).get(request, *args, **kwargs)
                else:
                    messages_alert = ['No tiene permisos para editar el reporte']
                    return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))
            else:
                messages_alert = ['No tiene permisos para editar el reporte']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Editar_reporte_analista(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de un reporte por parte de un
    Analista del sistema.
    """
    model = Reporte
    form_class = ReporteForm
    template_name = "registro/reporte_form_update.html"
    success_url = reverse_lazy('registro:consultar_reporte')
    success_message = "Se actualizo el reporte con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar el reporte no es el autor/creador.
        """
        self.object = self.get_object()
        if request.user.is_superuser:
            return super(Editar_reporte_analista, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para editar el reporte de tareas']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Borrar_reporte(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar un reporte registrado en el sistema.
    """
    model = Reporte
    success_url = reverse_lazy('registro:consultar_reporte')
    success_message = "Se elimino el reporte con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta borrar el reporte no es staff o el autor/creador.
        """
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        self.object = self.get_object()
        if request.user.is_staff:
            return self.render_to_response(context)
        else:
            if str(self.object) == str(self.request.user):
                return self.render_to_response(context)
            else:
                messages_alert = ['No tiene permisos para borrar el reporte']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))

    def delete(self, request, *args, **kwargs):
        """
        Función que permite mandar un mensaje al template
        cuando se borra un reporte y registra en la Bitácora que
        se elimino un reporte.
        """
        messages.success(self.request, self.success_message)
        return super(Borrar_reporte, self).delete(request, *args, **kwargs)


class Detallar_reporte(DetailView):
    """
    Clase que muestra la lista de entradas de la bitácora
    """
    model = Reporte
    template_name = "registro/reporte_detail.html"

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


###############################
##### Filtros de búsqueda #####
###############################

class Buscar_reporte(TemplateView):
    """
    Plantilla que tiene el formulario para buscar reportes.
    """
    template_name = "registro/buscar.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.user.is_superuser:
            return self.render_to_response(context)
        else:
            if request.user.is_staff:
                # messages_alert = ['No tiene permisos para acceder']
                # return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))
                return self.render_to_response(context)
            else:
                if request.user.is_active:
                    return self.render_to_response(context)


def busqueda(request):
    """
    Función que recibe los parámetros enviados desde el formulario de
    búsqueda de reportes y filtra los reportes con querysets.
    """
    if 'ano' in request.GET and request.GET['ano'] and 'mes' in request.GET and request.GET['mes']:
        ano = request.GET['ano']
        mes = request.GET['mes']
        reportes_ano = Reporte.objects.filter(ano__icontains=ano)
        if request.user.is_superuser:
            if ano == "Todos" and mes == "Todos":
                reportes = Reporte.objects.all()
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Enero":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Febrero":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Marzo":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Abril":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Mayo":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Junio":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Julio":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Agosto":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Septiembre":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Octubre":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Noviembre":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "Todos" and mes == "Diciembre":
                reportes = Reporte.objects.all().filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "2027" and mes == "Todos":
                reportes = reportes_ano.all().filter(ano__icontains=ano)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "2026" and mes == "Todos":
                reportes = reportes_ano.all().filter(ano__icontains=ano)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "2025" and mes == "Todos":
                reportes = reportes_ano.all().filter(ano__icontains=ano)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "2024" and mes == "Todos":
                reportes = reportes_ano.all().filter(ano__icontains=ano)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "2023" and mes == "Todos":
                reportes = reportes_ano.all().filter(ano__icontains=ano)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "2022" and mes == "Todos":
                reportes = reportes_ano.all().filter(ano__icontains=ano)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "2021" and mes == "Todos":
                reportes = reportes_ano.all().filter(ano__icontains=ano)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "2020" and mes == "Todos":
                reportes = reportes_ano.all().filter(ano__icontains=ano)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "2019" and mes == "Todos":
                reportes = reportes_ano.all().filter(ano__icontains=ano)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            if ano == "2018" and mes == "Todos":
                reportes = reportes_ano.all().filter(ano__icontains=ano)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            else:
                reportes = reportes_ano.filter(mes__icontains=mes)
                return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
        else:
            if request.user.is_staff:
                if ano == "Todos" and mes == "Todos":
                    reportes = Reporte.objects.all()
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Enero":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Febrero":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Marzo":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Abril":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Mayo":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Junio":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Julio":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Agosto":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Septiembre":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Octubre":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Noviembre":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Diciembre":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2027" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2026" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2025" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2024" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2023" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2022" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2021" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2020" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2019" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2018" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                else:
                    reportes = reportes_ano.filter(mes__icontains=mes)
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
            else:
                if ano == "Todos" and mes == "Todos":
                    reportes = Reporte.objects.all().filter(autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Enero":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Febrero":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Marzo":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Abril":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Mayo":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Junio":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Julio":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Agosto":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Septiembre":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Octubre":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Noviembre":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "Todos" and mes == "Diciembre":
                    reportes = Reporte.objects.all().filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2024" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2023" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2022" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2021" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2020" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2019" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                if ano == "2018" and mes == "Todos":
                    reportes = reportes_ano.all().filter(ano__icontains=ano, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
                else:
                    reportes = reportes_ano.filter(mes__icontains=mes, autor=str(request.user))
                    return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
    else:
        return HttpResponse('Por favor introduce un termino de búsqueda.')
