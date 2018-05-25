# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Reporte(models.Model):
    """
    Modelo de un Reporte de actividades de un proyecto.
    """
    nombre_proyecto = models.CharField(max_length=400, blank=True,null=True)
    nombre_caravisible = models.CharField(max_length=4000, blank=True,null=True)
    nombre_director = models.CharField(max_length=400, blank=True,null=True)
    mes = models.CharField(max_length=400, blank=True,null=True)
    ano = models.CharField(max_length=400, blank=True,null=True)
    desc_avance = models.CharField(max_length=5000, blank=True,null=True)
    obstaculos = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_1 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_1 = models.CharField(max_length=400, blank=True,null=True)
    act_rea_trab_1 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_1 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_2 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_2 = models.CharField(max_length=400, blank=True,null=True)
    act_rea_trab_2 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_2 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_3 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_3 = models.CharField(max_length=400, blank=True,null=True)
    act_rea_trab_3 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_3 = models.CharField(max_length=5000, blank=True,null=True)

    def __unicode__(self):
        return self.nombre_proyecto

    def get_absolute_url(self):
        return reverse('registro:editar_reporte', kwargs={'pk': self.pk})
