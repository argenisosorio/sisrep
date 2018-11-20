# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class ProyectoPoa(models.Model):
    """
    Modelo que contiene los campos de un Proyecto POA.
    """
    nombre_proyecto = models.CharField(max_length=4000, blank=True,null=True)

    def __unicode__(self):
        return self.nombre_proyecto

    def get_absolute_url(self):
        return reverse('safet:editar_reporte', kwargs={'pk': self.pk})
