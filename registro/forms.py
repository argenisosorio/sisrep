# -*- coding: utf-8 -*-
from django import forms
from registro.models import Reporte, Proyecto
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)
from datetime import *
from django.contrib.admin.widgets import AdminDateWidget
from base.constantes import *


class ProyectoForm(forms.ModelForm):
    """
    Formulario con los campos de un Proyecto.
    """
    nombre_proyecto = forms.CharField(label='Nombre del Proyecto', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    class Meta:

        model = Proyecto
        fields = '__all__'


class ReporteForm(forms.ModelForm):
    """
    Formulario con los campos de un Reporte de actividades de un proyecto.
    """

    def __init__(self, *args, **kwargs):
        """
        Método que carga la data de los proyectos registrados
        del modelo Proyecto en el campo nombre_proyecto del
        modelo Reporte.
        """
        super(ReporteForm, self).__init__(*args, **kwargs)
        lista_proyectos = Proyecto.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        self.fields['nombre_proyecto'] = forms.ChoiceField(label="Nombre del Proyecto", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_proyectos)

    autor = forms.CharField(label='Autor', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    nombre_caravisible = forms.CharField(label='Nombre completo del/la Cara Visible', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    nombre_director = forms.ChoiceField(label='Director de Proyecto', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = directores)

    mes = forms.ChoiceField(label='Mes', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = meses)

    ano = forms.ChoiceField(label='Año', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = anos)

    desc_avance = forms.CharField(label='Descripción General del Avance del Proyecto', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    obstaculos = forms.CharField(label='Dificultades y Obstáculos', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    nombre_trab_1 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    cargo_trab_1 = forms.ChoiceField(label='Cargo', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), choices = cargos, required = False)

    act_rea_trab_1 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_1 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_trab_2 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    cargo_trab_2 = forms.ChoiceField(label='Cargo', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), choices = cargos, required = False)

    act_rea_trab_2 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_2 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_trab_3 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    cargo_trab_3 = forms.ChoiceField(label='Cargo', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), choices = cargos, required = False)

    act_rea_trab_3 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_3 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    class Meta:

        model = Reporte
        fields = '__all__'
