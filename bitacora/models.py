# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Bitacora(models.Model):
    """
    Clase que contiene los campos del modelo de la
    bitácota que guarda los eventos de los usuarios.
    """
    entrada = models.CharField(max_length=200)

    def __unicode__(self):
        return self.entrada
