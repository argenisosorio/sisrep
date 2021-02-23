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
        return reverse('safet:editar_proyecto', kwargs={'pk': self.pk})


class AccionEspecifica(models.Model):
    """
    Modelo que contiene los campos de una Acción Específica.
    """
    nombre_accion = models.CharField(max_length=4000, blank=True,null=True)

    def __unicode__(self):
        return self.nombre_accion

    def get_absolute_url(self):
        return reverse('safet:editar_accion', kwargs={'pk': self.pk})


class ReporteAvances(models.Model):
    """
    Modelo que contiene los campos de un Reporte de Avances.
    """
    autor = models.CharField(max_length=400, blank=True,null=True)
    nombre_proyecto_poa = models.CharField(max_length=4000, blank=True,null=True)
    nombre_accion_especifica = models.CharField(max_length=4000, blank=True,null=True)
    nombre_producto = models.CharField(max_length=4000, blank=True,null=True)
    tipo_producto = models.CharField(max_length=4000, blank=True,null=True)
    ano_ejecucion = models.CharField(max_length=4000, blank=True,null=True)
    fecha_entrega = models.CharField(max_length=4000, blank=True,null=True)
    nombre_caravisible = models.CharField(max_length=4000, blank=True,null=True)
    nombre_director = models.CharField(max_length=4000, blank=True,null=True)
    integrantes_equipo = models.CharField(max_length=4000, blank=True,null=True)
    # Nombres de las actividades del Proyecto.
    nombre_act_1 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_2 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_3 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_4 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_5 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_6 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_7 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_8 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_9 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_10 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_11 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_12 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_13 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_14 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_15 = models.CharField(max_length=4000, blank=True,null=True)
    # Nombres de las actividades del proyecto.
    resp_act_1 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_2 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_3 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_4 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_5 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_6 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_7 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_8 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_9 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_10 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_11 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_12 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_13 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_14 = models.CharField(max_length=4000, blank=True,null=True)
    resp_act_15 = models.CharField(max_length=4000, blank=True,null=True)
    # Fechas de entrega de las actividades del proyecto.
    fecha_entrega_act_1 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_2 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_3 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_4 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_5 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_6 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_7 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_8 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_9 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_10 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_11 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_12 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_13 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_14 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_15 = models.CharField(max_length=100, blank=True,null=True)
    # Enlaces de verificación de las actividades del proyecto.
    enlace_ver_act_1 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_2 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_3 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_4 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_5 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_6 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_7 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_8 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_9 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_10 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_11 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_12 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_13 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_14 = models.CharField(max_length=500, blank=True,null=True)
    enlace_ver_act_15 = models.CharField(max_length=500, blank=True,null=True)
    # Porcentaje de las actividades del proyecto.
    porc_act_1 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_2 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_3 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_4 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_5 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_6 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_7 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_8 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_9 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_10 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_11 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_12 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_13 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_14 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_act_15 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    # Porcentaje de avance de las actividades del proyecto.
    porc_avan_act_1 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_2 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_3 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_4 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_5 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_6 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_7 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_8 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_9 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_10 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_11 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_12 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_13 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_14 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    porc_avan_act_15 = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)

    def sumatoria_por_avan(self):
        sumatoria_por_avan = self.porc_avan_act_1+self.porc_avan_act_2+self.porc_avan_act_3+self.porc_avan_act_4+self.porc_avan_act_5+self.porc_avan_act_6+self.porc_avan_act_7+self.porc_avan_act_8+self.porc_avan_act_9+self.porc_avan_act_10+self.porc_avan_act_11+self.porc_avan_act_12+self.porc_avan_act_13+self.porc_avan_act_14+self.porc_avan_act_15
        if sumatoria_por_avan <= 100:
            return str(sumatoria_por_avan)

    def __unicode__(self):
        return self.autor

    def get_absolute_url(self):
        return reverse('safet:editar_reporte_avances', kwargs={'pk': self.pk})
