# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Reporte(models.Model):
    """
    Modelo de un Reporte de actividades de un proyecto.
    """
    campo0 = models.CharField(max_length=3000, blank=True,null=True)
    campo1 = models.CharField(max_length=3000, blank=True,null=True)
    campo2 = models.CharField(max_length=3000, blank=True,null=True)
    campo3 = models.CharField(max_length=3000, blank=True,null=True)

    def __unicode__(self):
        return self.campo1

    def get_absolute_url(self):
        return reverse('registro:editar_reporte', kwargs={'pk': self.pk})
