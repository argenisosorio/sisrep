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
    Formulario con los campos de un proyecto poa.
    """
    nombre_proyecto = forms.CharField(label='Nombre del proyecto', widget=TextInput(attrs={
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
    nombre_accion = forms.CharField(label='Nombre de la acción específica', widget=TextInput(attrs={
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
        Método que permite inicializar los campos desplegables del formulario.
        """
        super(ReporteAvancesForm, self).__init__(*args, **kwargs)
        lista_proyectos_poa = ProyectoPoa.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_acciones_especificas = AccionEspecifica.objects.all().values_list('nombre_accion','nombre_accion')
        lista_productos = Proyecto.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_directores = Director.objects.all().values_list('nombre_director','nombre_director')
        lista_carasvisibles = Caravisible.objects.all().values_list('nombre_caravisible','nombre_caravisible')

        self.fields['nombre_proyecto_poa'] = forms.ChoiceField(label="Nombre del proyecto poa", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'disabled': 'disabled',
        }), choices=lista_proyectos_poa)

        self.fields['nombre_accion_especifica'] = forms.ChoiceField(label="Nombre de la acción específica", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_acciones_especificas)

        self.fields['nombre_producto'] = forms.ChoiceField(label="Nombre del producto", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_productos)

        self.fields['nombre_director'] = forms.ChoiceField(label="Nombre del director", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_directores)

        self.fields['nombre_caravisible'] = forms.ChoiceField(label="Nombre del cara visible", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_carasvisibles)

    autor = forms.CharField(label='Nombre de usuario que podrá cargar avances en este reporte', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    ano_ejecucion = forms.ChoiceField(label='Año de ejecución', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = anos)

    fecha_entrega = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    tipo_producto = forms.CharField(label='Tipo de producto', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    integrantes_equipo = forms.CharField(label='Integrantes del equipo', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'required': 'True',
    }), required = False)

    # Nombres de las actividades del proyecto.
    nombre_act_1 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_2 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_3 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_4 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_5 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_6 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_7 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_8 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_9 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_10 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_11 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_12 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_13 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_14 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_15 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Nombres de los responsables de las actividades.
    resp_act_1 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_2 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_3 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_4 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_5 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_6 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_7 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_8 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_9 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_10 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_11 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_12 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_13 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_14 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_15 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Fechas de entrega de las actividades de la planificación.
    fecha_entrega_act_1 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_2 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_3 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_4 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_5 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_6 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_7 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_8 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_9 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_10 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_11 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_12 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_13 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_14 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_15 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Enlaces de verificación de las actividades del proyecto.
    enlace_ver_act_1 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_2 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_3 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_4 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_5 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_6 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_7 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_8 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_9 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_10 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_11 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_12 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_13 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_14 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_15 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Ponderación asignada (%) de la planificación.
    porc_act_1 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_2 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_3 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_4 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_5 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_6 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_7 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_8 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_9 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_10 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_11 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_12 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_13 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_14 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_15 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    # Porcentaje de avance de la actividad.
    porc_avan_act_1 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_2 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_3 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_4 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_5 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_6 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_7 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_8 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_9 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_10 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_11 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_12 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_13 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_14 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_15 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    class Meta:

        model = ReporteAvances
        fields = '__all__'


class ReporteAvancesSoftwareForm(forms.ModelForm):
    """
    Modelo que contiene los campos de un Reporte de Avances de un producto
    del tipo Software.
    """

    def __init__(self, *args, **kwargs):
        """
        Método que permite inicializar los campos desplegables del formulario.
        """
        super(ReporteAvancesSoftwareForm, self).__init__(*args, **kwargs)
        lista_proyectos_poa = ProyectoPoa.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_acciones_especificas = AccionEspecifica.objects.all().values_list('nombre_accion','nombre_accion')
        lista_productos = Proyecto.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_directores = Director.objects.all().values_list('nombre_director','nombre_director')
        lista_carasvisibles = Caravisible.objects.all().values_list('nombre_caravisible','nombre_caravisible')

        self.fields['nombre_proyecto_poa'] = forms.ChoiceField(label="Nombre del proyecto poa", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'disabled': 'disabled',
        }), choices=lista_proyectos_poa)

        self.fields['nombre_accion_especifica'] = forms.ChoiceField(label="Nombre de la acción específica", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_acciones_especificas)

        self.fields['nombre_producto'] = forms.ChoiceField(label="Nombre del producto", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_productos)

        self.fields['nombre_director'] = forms.ChoiceField(label="Nombre del director", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_directores)

        self.fields['nombre_caravisible'] = forms.ChoiceField(label="Nombre del cara visible", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_carasvisibles)

    autor = forms.CharField(label='Nombre de usuario que podrá cargar avances en este reporte', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    ano_ejecucion = forms.ChoiceField(label='Año de ejecución', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = anos)

    fecha_entrega = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    tipo_producto = forms.CharField(label='Tipo de producto', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
        'value': 'Software',
    }), required = True)

    integrantes_equipo = forms.CharField(label='Integrantes del equipo', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'required': 'True',
    }), required = False)

    # Nombres de las actividades del proyecto.
    nombre_act_1 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Conceptualización',
    }), required = False)

    nombre_act_2 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Elaboración del Plan del proyecto',
    }), required = False)

    nombre_act_3 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Definición de Estándares de desarrollo',
    }), required = False)

    nombre_act_4 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Instalación de la Plataforma de gestión del proyecto',
    }), required = False)

    nombre_act_5 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Especificación de requerimientos',
    }), required = False)

    nombre_act_6 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Especificación de arquitectura de la aplicación',
    }), required = False)

    nombre_act_7 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Diseño del Prototipo no funcional',
    }), required = False)

    nombre_act_8 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Codificación de las funcionalidades',
    }), required = False)

    nombre_act_9 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Aplicación de las pruebas (funcionales, no funcionales, seguridad y rendimiento según sea el caso)',
    }), required = False)

    nombre_act_10 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Elaboración de manuales',
    }), required = False)

    nombre_act_11 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Empaquetado del software',
    }), required = False)

    nombre_act_12 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Publicación',
    }), required = False)

    nombre_act_13 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Procesos de Apropiación',
    }), required = False)

    nombre_act_14 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_15 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Nombres de los responsables de las actividades.
    resp_act_1 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_2 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_3 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_4 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_5 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_6 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_7 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_8 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_9 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_10 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_11 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_12 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_13 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_14 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_15 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Fechas de entrega de las actividades.
    fecha_entrega_act_1 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_2 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_3 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_4 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_5 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_6 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_7 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_8 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_9 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_10 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_11 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_12 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_13 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_14 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_15 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Enlaces de verificación de las actividades del proyecto.
    enlace_ver_act_1 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_2 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_3 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_4 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_5 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_6 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_7 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_8 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_9 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_10 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_11 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_12 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_13 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_14 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_15 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Porcentaje de las actividades del proyecto.
    porc_act_1 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_2 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_3 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_4 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_5 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_6 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_7 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_8 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_9 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_10 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_11 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_12 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_13 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_14 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_15 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    # Porcentaje de avance de las actividades del proyecto.
    porc_avan_act_1 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_2 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_3 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_4 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_5 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_6 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_7 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_8 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_9 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_10 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_11 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_12 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_13 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_14 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_15 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    class Meta:

        model = ReporteAvances
        fields = '__all__'


class ReporteAvancesCursoLineaForm(forms.ModelForm):
    """
    Modelo que contiene los campos de un Reporte de Avances de un producto
    del tipo Curso en Línea.
    """

    def __init__(self, *args, **kwargs):
        """
        Método que permite inicializar los campos desplegables del formulario.
        """
        super(ReporteAvancesCursoLineaForm, self).__init__(*args, **kwargs)
        lista_proyectos_poa = ProyectoPoa.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_acciones_especificas = AccionEspecifica.objects.all().values_list('nombre_accion','nombre_accion')
        lista_productos = Proyecto.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_directores = Director.objects.all().values_list('nombre_director','nombre_director')
        lista_carasvisibles = Caravisible.objects.all().values_list('nombre_caravisible','nombre_caravisible')

        self.fields['nombre_proyecto_poa'] = forms.ChoiceField(label="Nombre del proyecto poa", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'disabled': 'disabled',
        }), choices=lista_proyectos_poa)

        self.fields['nombre_accion_especifica'] = forms.ChoiceField(label="Nombre de la acción específica", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_acciones_especificas)

        self.fields['nombre_producto'] = forms.ChoiceField(label="Nombre del producto", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_productos)

        self.fields['nombre_director'] = forms.ChoiceField(label="Nombre del director", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_directores)

        self.fields['nombre_caravisible'] = forms.ChoiceField(label="Nombre del cara visible", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_carasvisibles)

    autor = forms.CharField(label='Nombre de usuario que podrá cargar avances en este reporte', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    ano_ejecucion = forms.ChoiceField(label='Año de ejecución', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = anos)

    fecha_entrega = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    tipo_producto = forms.CharField(label='Tipo de producto', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
        'value': 'Curso en Línea',
    }), required = True)

    integrantes_equipo = forms.CharField(label='Integrantes del equipo', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'required': 'True',
    }), required = False)

    # Nombres de las actividades del proyecto.
    nombre_act_1 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Conceptualización o Justificación',
    }), required = False)

    nombre_act_2 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Diseño Instruccional',
    }), required = False)

    nombre_act_3 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Desarrollo de objetos de aprendizaje',
    }), required = False)

    nombre_act_4 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Montaje del Curso en la Plataforma',
    }), required = False)

    nombre_act_5 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Pruebas',
    }), required = False)

    nombre_act_6 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Validación',
    }), required = False)

    nombre_act_7 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Implementación del Curso',
    }), required = False)

    nombre_act_8 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Gestión de Certificados',
    }), required = False)

    nombre_act_9 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Evaluación de la Implementación del Curso',
    }), required = False)

    nombre_act_10 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Procesos de Apropiación ',
    }), required = False)

    nombre_act_11 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_12 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_13 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_14 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_15 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Nombres de los responsables de las actividades del proyecto.
    resp_act_1 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_2 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_3 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_4 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_5 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_6 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_7 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_8 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_9 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_10 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_11 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_12 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_13 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_14 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_15 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Fechas de entrega de las actividades del proyecto.
    fecha_entrega_act_1 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_2 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_3 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_4 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_5 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_6 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_7 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_8 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_9 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_10 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_11 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_12 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_13 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_14 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_15 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Enlaces de verificación de las actividades del proyecto.
    enlace_ver_act_1 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_2 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_3 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_4 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_5 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_6 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_7 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_8 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_9 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_10 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_11 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_12 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_13 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_14 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_15 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Porcentaje de las actividades del proyecto.
    porc_act_1 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_2 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_3 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_4 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_5 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_6 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_7 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_8 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_9 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_10 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_11 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_12 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_13 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_14 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_15 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    # Porcentaje de avance de las actividades del proyecto.
    porc_avan_act_1 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_2 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_3 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_4 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_5 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_6 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_7 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_8 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_9 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_10 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_11 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_12 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_13 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_14 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_15 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    class Meta:

        model = ReporteAvances
        fields = '__all__'


class ReporteAvancesJornadaForm(forms.ModelForm):
    """
    Modelo que contiene los campos de un Reporte de Avances de un producto
    del tipo Jornada.
    """

    def __init__(self, *args, **kwargs):
        """
        Método que permite inicializar los campos desplegables del formulario.
        """
        super(ReporteAvancesJornadaForm, self).__init__(*args, **kwargs)
        lista_proyectos_poa = ProyectoPoa.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_acciones_especificas = AccionEspecifica.objects.all().values_list('nombre_accion','nombre_accion')
        lista_productos = Proyecto.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_directores = Director.objects.all().values_list('nombre_director','nombre_director')
        lista_carasvisibles = Caravisible.objects.all().values_list('nombre_caravisible','nombre_caravisible')

        self.fields['nombre_proyecto_poa'] = forms.ChoiceField(label="Nombre del proyecto poa", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'disabled': 'disabled',
        }), choices=lista_proyectos_poa)

        self.fields['nombre_accion_especifica'] = forms.ChoiceField(label="Nombre de la acción específica", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_acciones_especificas)

        self.fields['nombre_producto'] = forms.ChoiceField(label="Nombre del producto", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_productos)

        self.fields['nombre_director'] = forms.ChoiceField(label="Nombre del director", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_directores)

        self.fields['nombre_caravisible'] = forms.ChoiceField(label="Nombre del cara visible", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_carasvisibles)

    autor = forms.CharField(label='Nombre de usuario que podrá cargar avances en este reporte', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    ano_ejecucion = forms.ChoiceField(label='Año de ejecución', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = anos)

    fecha_entrega = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    tipo_producto = forms.CharField(label='Tipo de producto', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
        'value': 'Jornada',
    }), required = True)

    integrantes_equipo = forms.CharField(label='Integrantes del equipo', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'required': 'True',
    }), required = False)

    # Nombres de las actividades del proyecto.
    nombre_act_1 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Conceptualización',
    }), required = False)

    nombre_act_2 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Organización',
    }), required = False)

    nombre_act_3 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Logística',
    }), required = False)

    nombre_act_4 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Ejecución, sistematización y registro de la jornada',
    }), required = False)

    nombre_act_5 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Contenidos a socializar',
    }), required = False)

    nombre_act_6 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Procesos de socialización',
    }), required = False)

    nombre_act_7 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_8 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_9 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_10 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_11 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_12 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_13 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_14 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_15 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Nombres de los responsables de las actividades del proyecto.
    resp_act_1 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_2 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_3 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_4 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_5 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_6 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_7 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_8 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_9 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_10 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_11 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_12 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_13 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_14 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_15 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Enlaces de verificación de las actividades del proyecto.
    enlace_ver_act_1 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_2 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_3 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_4 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_5 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_6 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_7 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_8 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_9 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_10 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_11 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_12 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_13 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_14 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_15 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Fechas de entrega de las actividades del proyecto.
    fecha_entrega_act_1 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_2 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_3 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_4 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_5 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_6 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_7 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_8 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_9 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_10 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_11 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_12 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_13 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_14 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_15 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Porcentaje de las actividades del proyecto.
    porc_act_1 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_2 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_3 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_4 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_5 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_6 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_7 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_8 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_9 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_10 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_11 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_12 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_13 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_14 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_15 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    # Porcentaje de avance de las actividades del proyecto.
    porc_avan_act_1 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_2 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_3 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_4 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_5 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_6 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_7 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_8 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_9 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_10 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_11 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_12 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_13 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_14 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_15 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    class Meta:

        model = ReporteAvances
        fields = '__all__'


class ReporteAvancesPublicacionForm(forms.ModelForm):
    """
    Modelo que contiene los campos de un Reporte de Avances de un producto
    del tipo Jornada.
    """

    def __init__(self, *args, **kwargs):
        """
        Método que permite inicializar los campos desplegables del formulario.
        """
        super(ReporteAvancesPublicacionForm, self).__init__(*args, **kwargs)
        lista_proyectos_poa = ProyectoPoa.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_acciones_especificas = AccionEspecifica.objects.all().values_list('nombre_accion','nombre_accion')
        lista_productos = Proyecto.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_directores = Director.objects.all().values_list('nombre_director','nombre_director')
        lista_carasvisibles = Caravisible.objects.all().values_list('nombre_caravisible','nombre_caravisible')

        self.fields['nombre_proyecto_poa'] = forms.ChoiceField(label="Nombre del proyecto poa", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'disabled': 'disabled',
        }), choices=lista_proyectos_poa)

        self.fields['nombre_accion_especifica'] = forms.ChoiceField(label="Nombre de la acción específica", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_acciones_especificas)

        self.fields['nombre_producto'] = forms.ChoiceField(label="Nombre del producto", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_productos)

        self.fields['nombre_director'] = forms.ChoiceField(label="Nombre del director", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_directores)

        self.fields['nombre_caravisible'] = forms.ChoiceField(label="Nombre del cara visible", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_carasvisibles)

    autor = forms.CharField(label='Nombre de usuario que podrá cargar avances en este reporte', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    ano_ejecucion = forms.ChoiceField(label='Año de ejecución', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = anos)

    fecha_entrega = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    tipo_producto = forms.CharField(label='Tipo de producto', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
        'value': 'Publicación',
    }), required = True)

    integrantes_equipo = forms.CharField(label='Integrantes del equipo', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'required': 'True',
    }), required = False)

    # Nombres de las actividades del proyecto.
    nombre_act_1 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Conceptualización',
    }), required = False)

    nombre_act_2 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Convocatoria a publicar',
    }), required = False)

    nombre_act_3 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Recepción revista comité editorial',
    }), required = False)

    nombre_act_4 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Arbitraje',
    }), required = False)

    nombre_act_5 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Edición',
    }), required = False)

    nombre_act_6 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Publicación',
    }), required = False)

    nombre_act_7 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': 'Procesos de Apropiación',
    }), required = False)

    nombre_act_8 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_9 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_10 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_11 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_12 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_13 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_14 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_15 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Nombres de los responsables de las actividades del proyecto.
    resp_act_1 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_2 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_3 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_4 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_5 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_6 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_7 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_8 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_9 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_10 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_11 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_12 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_13 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_14 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_15 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Enlaces de verificación de las actividades del proyecto.
    enlace_ver_act_1 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_2 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_3 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_4 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_5 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_6 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_7 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_8 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_9 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_10 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_11 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_12 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_13 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_14 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_15 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Fechas de entrega de las actividades del proyecto.
    fecha_entrega_act_1 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_2 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_3 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_4 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_5 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_6 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_7 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_8 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_9 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_10 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_11 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_12 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_13 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_14 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_15 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Porcentaje de las actividades del proyecto.
    porc_act_1 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_2 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_3 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_4 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_5 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_6 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_7 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_8 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_9 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_10 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_11 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_12 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_13 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_14 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_act_15 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    # Porcentaje de avance de las actividades del proyecto.
    porc_avan_act_1 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_2 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_3 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_4 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_5 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_6 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_7 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_8 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_9 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_10 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_11 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_12 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_13 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_14 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_15 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    class Meta:

        model = ReporteAvances
        fields = '__all__'


class ReporteAvancesCVForm(forms.ModelForm):
    """
    Modelo que contiene los campos de un Reporte de Avances que
    puede ver un CV.
    """

    def __init__(self, *args, **kwargs):
        """
        Método que permite inicializar los campos desplegables del formulario.
        """
        super(ReporteAvancesCVForm, self).__init__(*args, **kwargs)
        lista_proyectos_poa = ProyectoPoa.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_acciones_especificas = AccionEspecifica.objects.all().values_list('nombre_accion','nombre_accion')
        lista_productos = Proyecto.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        lista_directores = Director.objects.all().values_list('nombre_director','nombre_director')
        lista_carasvisibles = Caravisible.objects.all().values_list('nombre_caravisible','nombre_caravisible')

        self.fields['nombre_proyecto_poa'] = forms.ChoiceField(label="Nombre del proyecto poa", widget=Select(attrs={
            'class':'form-control input-md disabled-input',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_proyectos_poa)

        self.fields['nombre_accion_especifica'] = forms.ChoiceField(label="Nombre de la acción específica", widget=Select(attrs={
            'class':'form-control input-md disabled-input',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'disabled': 'disabled',
        }), choices=lista_acciones_especificas)

        self.fields['nombre_producto'] = forms.ChoiceField(label="Nombre del producto", widget=Select(attrs={
            'class':'form-control input-md disabled-input',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'disabled': 'disabled',
        }), choices=lista_productos)

        self.fields['nombre_director'] = forms.ChoiceField(label="Nombre del director", widget=Select(attrs={
            'class':'form-control input-md disabled-input',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'disabled': 'disabled',
        }), choices=lista_directores)

        self.fields['nombre_caravisible'] = forms.ChoiceField(label="Nombre del cara visible", widget=Select(attrs={
            'class':'form-control input-md disabled-input',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'disabled': 'disabled',
        }), choices=lista_carasvisibles)

    autor = forms.CharField(label='Nombre de usuario que podrá cargar avances en este reporte', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: none;',
        'required': 'True',
        #'disabled': 'disabled',
    }), required = True)

    ano_ejecucion = forms.ChoiceField(label='Año de ejecución', widget=Select(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
        #'disabled': 'disabled',
    }), choices = anos)

    fecha_entrega = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
        #'disabled': 'disabled',
    }), required = True)

    tipo_producto = forms.CharField(label='Tipo de producto', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
        #'disabled': 'disabled',
        #'readonly':'true'
    }), required = True)

    integrantes_equipo = forms.CharField(label='Integrantes del equipo', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'required': 'True',
    }), required = False)

    # Nombres de las actividades del proyecto.
    nombre_act_1 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_2 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_3 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_4 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_5 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_6 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_7 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_8 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_9 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_10 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_11 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_12 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_13 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_14 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    nombre_act_15 = forms.CharField(label='Nombre de la actividad', widget=TextInput(attrs={
        'class':'form-control input-md disabled-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'disabled': 'disabled',
    }), required = False)

    # Nombres de los responsables de las actividades.
    resp_act_1 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_2 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_3 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_4 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_5 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_6 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_7 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_8 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_9 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_10 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_11 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_12 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_13 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_14 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    resp_act_15 = forms.CharField(label='Nombre del responsable', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Enlaces de verificación de las actividades del proyecto.
    enlace_ver_act_1 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_2 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_3 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_4 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_5 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_6 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_7 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_8 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_9 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_10 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_11 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_12 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_13 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_14 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlace_ver_act_15 = forms.CharField(label='Enlace de verificación', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Fechas de entrega de las actividades del proyecto.
    fecha_entrega_act_1 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_2 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_3 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_4 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_5 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_6 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_7 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_8 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_9 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_10 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_11 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_12 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_13 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_14 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_15 = forms.CharField(label='Fecha de entrega', widget=TextInput(attrs={
        'class':'form-control input-md fechas',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Porcentaje de las actividades del proyecto.
    porc_act_1 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_2 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_3 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_4 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_5 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_6 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_7 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_8 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_9 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_10 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_11 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_12 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_13 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_14 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_15 = forms.CharField(label='Ponderación asignada (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Porcentaje de avance de las actividades del proyecto.
    porc_avan_act_1 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_2 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_3 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_4 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_5 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_6 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_7 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_8 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_9 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_10 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_11 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_12 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_13 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_14 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    porc_avan_act_15 = forms.CharField(label='Porcentaje de avance (%)', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'value': '0',
    }), required = False)

    class Meta:

        model = ReporteAvances
        fields = '__all__'