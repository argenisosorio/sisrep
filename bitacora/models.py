# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Bitacora(models.Model):
    """
    Clase que contiene los campos del modelo de la
    bitácota que guarda los eventos de los usuarios.
    """
    usuario = models.CharField(max_length=200)
    accion = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)

    def __unicode__(self):
        return self.accion
