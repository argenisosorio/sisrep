# -*- coding: utf-8 -*-
from django import forms
from safet.models import ProyectoPoa, AccionEspecifica, ReporteAvances
from registro.models import Proyecto, Director, Caravisible
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


class ReporteAvancesForm(forms.ModelForm):
    """
    Modelo que contiene los campos de un Reporte de Avances.
    """

    def __init__(self, *args, **kwargs):
        """
        Método que carga la data de los proyectos registrados
        del modelo Proyecto en el campo nombre_proyecto del
        modelo Reporte.
        """
        super(ReporteAvancesForm, self).__init__(*args, **kwargs)
        lista_proyectos_poa = ProyectoPoa.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_acciones_especificas = AccionEspecifica.objects.all().values_list('nombre_accion','nombre_accion')
        lista_productos = Proyecto.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_directores = Director.objects.all().values_list('nombre_director','nombre_director')
        lista_carasvisibles = Caravisible.objects.all().values_list('nombre_caravisible','nombre_caravisible')

        self.fields['nombre_proyecto_poa'] = forms.ChoiceField(label="Nombre del Proyecto POA", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'disabled': 'disabled',
        }), choices=lista_proyectos_poa)

        self.fields['nombre_accion_especifica'] = forms.ChoiceField(label="Nombre de la Acción Específica", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_acciones_especificas)

        self.fields['nombre_producto'] = forms.ChoiceField(label="Nombre del Producto", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_productos)

        self.fields['nombre_director'] = forms.ChoiceField(label="Nombre del Director", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_directores)

        self.fields['nombre_caravisible'] = forms.ChoiceField(label="Nombre del Cara Visible", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_carasvisibles)

    ano_ejecucion = forms.ChoiceField(label='Año de Ejecución', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = anos)

    fecha_entrega = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    integrantes_equipo = forms.CharField(label='Integrantes del equipo', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    # Nombres de las actividades del proyecto.
    nombre_act_1 = forms.CharField(label='Nombre de la Actividad 1', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_2 = forms.CharField(label='Nombre de la Actividad 2', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_3 = forms.CharField(label='Nombre de la Actividad 3', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_4 = forms.CharField(label='Nombre de la Actividad 4', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_5 = forms.CharField(label='Nombre de la Actividad 5', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_6 = forms.CharField(label='Nombre de la Actividad 6', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_7 = forms.CharField(label='Nombre de la Actividad 7', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_8 = forms.CharField(label='Nombre de la Actividad 8', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_9 = forms.CharField(label='Nombre de la Actividad 9', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_10 = forms.CharField(label='Nombre de la Actividad 10', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_11 = forms.CharField(label='Nombre de la Actividad 11', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_12 = forms.CharField(label='Nombre de la Actividad 12', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_13 = forms.CharField(label='Nombre de la Actividad 13', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_14 = forms.CharField(label='Nombre de la Actividad 14', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_15 = forms.CharField(label='Nombre de la Actividad 15', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Nombres de las actividades del proyecto.
    resp_act_1 = forms.CharField(label='Responsable de la Actividad 1', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_2 = forms.CharField(label='Responsable de la Actividad 2', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_3 = forms.CharField(label='Responsable de la Actividad 3', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_4 = forms.CharField(label='Responsable de la Actividad 4', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_5 = forms.CharField(label='Responsable de la Actividad 5', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_6 = forms.CharField(label='Responsable de la Actividad 6', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_7 = forms.CharField(label='Responsable de la Actividad 7', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_8 = forms.CharField(label='Responsable de la Actividad 8', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_9 = forms.CharField(label='Responsable de la Actividad 9', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_10 = forms.CharField(label='Responsable de la Actividad 10', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_11 = forms.CharField(label='Responsable de la Actividad 11', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_12 = forms.CharField(label='Responsable de la Actividad 12', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_13 = forms.CharField(label='Responsable de la Actividad 13', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_14 = forms.CharField(label='Responsable de la Actividad 14', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_15 = forms.CharField(label='Responsable de la Actividad 15', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Fechas de entrega de las actividades del proyecto.
    fecha_entrega_act_1 = forms.CharField(label='Fecha de entrega de la Actividad 1', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_2 = forms.CharField(label='Fecha de entrega de la Actividad 2', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_3 = forms.CharField(label='Fecha de entrega de la Actividad 3', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_4 = forms.CharField(label='Fecha de entrega de la Actividad 4', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_5 = forms.CharField(label='Fecha de entrega de la Actividad 5', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_6 = forms.CharField(label='Fecha de entrega de la Actividad 6', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_7 = forms.CharField(label='Fecha de entrega de la Actividad 7', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_8 = forms.CharField(label='Fecha de entrega de la Actividad 8', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_9 = forms.CharField(label='Fecha de entrega de la Actividad 9', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_10 = forms.CharField(label='Fecha de entrega de la Actividad 10', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_11 = forms.CharField(label='Fecha de entrega de la Actividad 11', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_12 = forms.CharField(label='Fecha de entrega de la Actividad 12', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_13 = forms.CharField(label='Fecha de entrega de la Actividad 13', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_14 = forms.CharField(label='Fecha de entrega de la Actividad 14', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_15 = forms.CharField(label='Fecha de entrega de la Actividad 15', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Porcentaje de las actividades del proyecto.
    porc_act_1 = forms.CharField(label='Porcentaje de la Actividad 1', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_2 = forms.CharField(label='Porcentaje de la Actividad 2', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_3 = forms.CharField(label='Porcentaje de la Actividad 3', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_4 = forms.CharField(label='Porcentaje de la Actividad 4', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_5 = forms.CharField(label='Porcentaje de la Actividad 5', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_6 = forms.CharField(label='Porcentaje de la Actividad 6', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_7 = forms.CharField(label='Porcentaje de la Actividad 7', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_8 = forms.CharField(label='Porcentaje de la Actividad 8', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_9 = forms.CharField(label='Porcentaje de la Actividad 9', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_10 = forms.CharField(label='Porcentaje de la Actividad 10', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_11 = forms.CharField(label='Porcentaje de la Actividad 11', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_12 = forms.CharField(label='Porcentaje de la Actividad 12', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_13 = forms.CharField(label='Porcentaje de la Actividad 13', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_14 = forms.CharField(label='Porcentaje de la Actividad 14', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_15 = forms.CharField(label='Porcentaje de la Actividad 15', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Porcentaje de avance de las actividades del proyecto.
    porc_avan_act_1 = forms.CharField(label='Porcentaje de avance la Actividad 1', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_2 = forms.CharField(label='Porcentaje de avance la Actividad 2', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_3 = forms.CharField(label='Porcentaje de avance la Actividad 3', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_4 = forms.CharField(label='Porcentaje de avance la Actividad 4', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_5 = forms.CharField(label='Porcentaje de avance la Actividad 5', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_6 = forms.CharField(label='Porcentaje de avance la Actividad 6', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_7 = forms.CharField(label='Porcentaje de avance la Actividad 7', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_8 = forms.CharField(label='Porcentaje de avance la Actividad 8', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_9 = forms.CharField(label='Porcentaje de avance la Actividad 9', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_10 = forms.CharField(label='Porcentaje de avance la Actividad 10', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_11 = forms.CharField(label='Porcentaje de avance la Actividad 11', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_12 = forms.CharField(label='Porcentaje de avance la Actividad 12', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_13 = forms.CharField(label='Porcentaje de avance la Actividad 13', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_14 = forms.CharField(label='Porcentaje de avance la Actividad 14', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_15 = forms.CharField(label='Porcentaje de avance la Actividad 15', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    class Meta:

        model = ReporteAvances
        fields = '__all__'
