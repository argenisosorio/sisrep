# -*- coding: utf-8 -*-
from django import forms
from safet.models import ProyectoPoa, AccionEspecifica
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)
from datetime import *
from django.contrib.admin.widgets import AdminDateWidget
from base.constantes import *


class ProyectoPoaForm(forms.ModelForm):
    """
    Formulario con los campos de un Proyecto POA.
    """
    nombre_proyecto = forms.CharField(label='Nombre del Proyecto', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    class Meta:

        model = ProyectoPoa
        fields = '__all__'


class AccionEspecificaForm(forms.ModelForm):
    """
    Formulario con los campos de una Acción Específica.
    """
    nombre_accion = forms.CharField(label='Nombre de la Acción Específica', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    class Meta:

        model = AccionEspecifica
        fields = '__all__'
