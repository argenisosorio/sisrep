# -*- coding: utf-8 -*-
from django.views.generic import ListView
from bitacora.models import Bitacora
from django.shortcuts import render_to_response
from django.template import RequestContext
#is_active = Cara visible
#is_staff = Director
#is_superuser = Analista


class Bitacora(ListView):
    """
    Clase que permite consultar la lista eventos de la bitácora.
    """
    model = Bitacora
    template_name = "bitacora/eventos.html"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta ver la bitácora no es superusuario.
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
            messages_alert = ['No tiene permisos para ver la Bitácora']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()
            queryset = queryset.order_by('-id')[:100] # Ordenando los objetos cronológicamente y mostrando solo los ultimos 100.
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
        return queryset
