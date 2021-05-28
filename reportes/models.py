# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

class Indicadores (models.Model):
    """
    Modelo que contiene los campos de los indicadores
    """

    # Beneficio
    ano_beneficio = models.CharField(max_length=400, blank=True,null=True)
    mes_beneficio = models.CharField(max_length=400, blank=True,null=True)
    beneficio = models.CharField(max_length=400, blank=True,null=True)
    cantidad = models.PositiveIntegerField(default=0, blank=True,null=True)
    # Impacto
    social = models.CharField(max_length=400, blank=True,null=True)
    economico = models.CharField(max_length=400, blank=True,null=True)
    productivo = models.CharField(max_length=400, blank=True,null=True)
    ambiental = models.CharField(max_length=400, blank=True,null=True)
    # Beneficiarios
    quienes = models.CharField(max_length=400, blank=True,null=True)
    cuantos = models.PositiveIntegerField(default=0, blank=True,null=True)
    
    def __unicode__(self):
        return self.quienes
