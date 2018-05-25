# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Bien(models.Model):
    """
    Modelo de un bien de CENDITEL.
    """
    campo0 = models.CharField(max_length=3000, blank=True,null=True)
    campo1 = models.CharField(max_length=3000, blank=True,null=True)
    campo2 = models.CharField(max_length=3000, blank=True,null=True)
    campo3 = models.CharField(max_length=3000, blank=True,null=True)
    campo4 = models.CharField(max_length=3000, blank=True,null=True)
    campo5 = models.CharField(max_length=3000, blank=True,null=True)
    campo6 = models.CharField(max_length=3000, blank=True,null=True)
    campo7 = models.CharField(max_length=3000, blank=True,null=True)
    campo8 = models.CharField(max_length=3000, blank=True,null=True)
    campo9 = models.CharField(max_length=3000, blank=True,null=True)
    campo10 = models.CharField(max_length=3000, blank=True,null=True)
    campo11 = models.CharField(max_length=3000, blank=True,null=True)
    campo12 = models.CharField(max_length=3000, blank=True,null=True)
    campo13 = models.CharField(max_length=3000, blank=True,null=True)

    def __unicode__(self):
        return self.campo1

    def get_absolute_url(self):
        return reverse('registro:editar_bien', kwargs={'pk': self.pk})
