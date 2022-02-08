# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Proyecto(models.Model):
    """
    Modelo que contiene los campos de un Proyecto.
    """
    nombre_proyecto = models.CharField(max_length=400, blank=True,null=True)

    def __unicode__(self):
        return self.nombre_proyecto

    def get_absolute_url(self):
        return reverse('registro:editar_reporte', kwargs={'pk': self.pk})


class Caravisible(models.Model):
    """
    Modelo que contiene los campos de un Proyecto.
    """
    nombre_caravisible = models.CharField(max_length=400, blank=True,null=True)

    def __unicode__(self):
        return self.nombre_caravisible

    def get_absolute_url(self):
        return reverse('registro:editar_cara_visible', kwargs={'pk': self.pk})


class Director(models.Model):
    """
    Modelo que contiene los campos de un Director.
    """
    nombre_director = models.CharField(max_length=400, blank=True,null=True)

    def __unicode__(self):
        return self.nombre_director

    def get_absolute_url(self):
        return reverse('registro:editar_director', kwargs={'pk': self.pk})


class Cargo(models.Model):
    """
    Modelo que contiene los campos de un Cargo.
    """
    nombre_cargo = models.CharField(max_length=400, blank=True,null=True)

    def __unicode__(self):
        return self.nombre_cargo

    def get_absolute_url(self):
        return reverse('registro:editar_cargo', kwargs={'pk': self.pk})


class Reporte(models.Model):
    """
    Modelo de un Reporte de actividades de un proyecto.
    """
    autor = models.CharField(max_length=400, blank=True,null=True)
    nombre_proyecto = models.CharField(max_length=400, blank=True,null=True)
    nombre_caravisible = models.CharField(max_length=4000, blank=True,null=True)
    nombre_director = models.CharField(max_length=400, blank=True,null=True)
    mes = models.CharField(max_length=400, blank=True,null=True)
    ano = models.CharField(max_length=400, blank=True,null=True)
    desc_avance = models.CharField(max_length=5000, blank=True,null=True)
    obstaculos = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_1 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_1 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_1 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_1 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_1 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_2 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_2 = models.CharField(max_length=400, blank=True,null=True)
    act_rea_trab_2 = models.CharField(max_length=5000, blank=True,null=True)
    act_asig_trab_2 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_2 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_3 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_3 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_3 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_3 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_3 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_4 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_4 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_4 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_4 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_4 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_5 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_5 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_5 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_5 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_5 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_6 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_6 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_6 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_6 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_6 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_7 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_7 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_7 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_7 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_7 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_8 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_8 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_8 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_8 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_8 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_9 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_9 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_9 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_9 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_9 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_10 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_10 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_10 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_10 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_10 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_11 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_11 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_11 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_11 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_11 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_12 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_12 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_12 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_12 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_12 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_13 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_13 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_13 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_13 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_13 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_14 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_14 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_14 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_14 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_14 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_15 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_15 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_15 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_15 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_15 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_16 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_16 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_16 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_16 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_16 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_17 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_17 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_17 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_17 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_17 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_18 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_18 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_18 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_18 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_18 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_19 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_19 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_19 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_19 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_19 = models.CharField(max_length=5000, blank=True,null=True)
    nombre_trab_20 = models.CharField(max_length=400, blank=True,null=True)
    cargo_trab_20 = models.CharField(max_length=400, blank=True,null=True)
    act_asig_trab_20 = models.CharField(max_length=5000, blank=True,null=True)
    act_rea_trab_20 = models.CharField(max_length=5000, blank=True,null=True)
    enlaces_trab_20 = models.CharField(max_length=5000, blank=True,null=True)
    fecha_registro_reporte = models.DateField(default=datetime.now)
    estatus = models.CharField(max_length=400,default="act")

    def __unicode__(self):
        return self.autor

    def get_absolute_url(self):
        return reverse('registro:editar_reporte', kwargs={'pk': self.pk})
