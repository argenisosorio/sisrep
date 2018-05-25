# -*- coding: utf-8 -*-
from django import forms
from registro.models import Reporte
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)
from datetime import *
from django.contrib.admin.widgets import AdminDateWidget

estados = (
    ('-', '-'),
    ('Operativo','Operativo'),
    ('Averiado','Averiado'),
    ('En reparación','En reparación'),
    ('Desuso','Desuso'),
    ('Desincorporado','Desincorporado'),
)

class ReporteForm(forms.ModelForm):
    """
    Formulario con los campos de un Reporte de actividades de un proyecto.
    """
    campo0 = forms.CharField(label='0', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo4,
    }), required = False)

    campo1 = forms.CharField(label='1', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo4,
    }), required = False)

    campo2 = forms.ChoiceField(label='2', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), choices = estados)

    campo3 = forms.CharField(label='3', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo12,
    }), required = False)

    class Meta:

        model = Reporte
        fields = '__all__'
