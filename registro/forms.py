# -*- coding: utf-8 -*-
from django import forms
from registro.models import Reporte, Proyecto, Caravisible, Director, Cargo
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)
from datetime import *
from django.contrib.admin.widgets import AdminDateWidget
from base.constantes import *


class ProyectoForm(forms.ModelForm):
    """
    Formulario con los campos de un producto.
    """
    nombre_proyecto = forms.CharField(label='Nombre del producto', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    class Meta:

        model = Proyecto
        fields = '__all__'


class CaravisibleForm(forms.ModelForm):
    """
    Formulario con los campos de un cara visible.
    """
    nombre_caravisible = forms.CharField(label='Nombre y Apellido del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    class Meta:

        model = Caravisible
        fields = '__all__'


class DirectorForm(forms.ModelForm):
    """
    Formulario con los campos de un director.
    """
    nombre_director = forms.CharField(label='Nombre del director', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    class Meta:

        model = Director
        fields = '__all__'


class CargoForm(forms.ModelForm):
    """
    Formulario con los campos de un cargo.
    """
    nombre_cargo = forms.CharField(label='Nombre del cargo', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    class Meta:

        model = Cargo
        fields = '__all__'


class ReporteForm(forms.ModelForm):
    """
    Formulario con los campos de un reporte de actividades de un reporte.
    """
    def __init__(self, *args, **kwargs):
        """
        Método que carga la data de los proyectos, caras visibles y directores
        registrados del modelo Proyecto en el campo nombre_proyecto del
        modelo Reporte.
        """
        super(ReporteForm, self).__init__(*args, **kwargs)
        lista_proyectos = Proyecto.objects.all().order_by('nombre_proyecto').values_list('nombre_proyecto','nombre_proyecto')
        lista_caravisibles = Caravisible.objects.all().order_by('nombre_caravisible').values_list('nombre_caravisible','nombre_caravisible')
        lista_directores = Director.objects.all().order_by('nombre_director').values_list('nombre_director','nombre_director')
        lista_cargos = Cargo.objects.all().order_by('nombre_cargo').values_list('nombre_cargo','nombre_cargo')

        self.fields['nombre_proyecto'] = forms.ChoiceField(label="Producto", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_proyectos)

        self.fields['nombre_caravisible'] = forms.ChoiceField(label="Cara visible", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        self.fields['nombre_director'] = forms.ChoiceField(label="Director", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_directores)

        #----------------------------
        # Nombres de los trabajadores
        #----------------------------

        # Trabajador 1
        self.fields['nombre_trab_1'] = forms.ChoiceField(label="Trabajador 1", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 2
        self.fields['nombre_trab_2'] = forms.ChoiceField(label="Trabajador 2", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 3
        self.fields['nombre_trab_3'] = forms.ChoiceField(label="Trabajador 3", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 4
        self.fields['nombre_trab_4'] = forms.ChoiceField(label="Trabajador 4", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 5
        self.fields['nombre_trab_5'] = forms.ChoiceField(label="Trabajador 5", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 6
        self.fields['nombre_trab_6'] = forms.ChoiceField(label="Trabajador 6", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 7
        self.fields['nombre_trab_7'] = forms.ChoiceField(label="Trabajador 7", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 8
        self.fields['nombre_trab_8'] = forms.ChoiceField(label="Trabajador 8", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 9
        self.fields['nombre_trab_9'] = forms.ChoiceField(label="Trabajador 9", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 10
        self.fields['nombre_trab_10'] = forms.ChoiceField(label="Trabajador 10", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 11
        self.fields['nombre_trab_11'] = forms.ChoiceField(label="Trabajador 11", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 12
        self.fields['nombre_trab_12'] = forms.ChoiceField(label="Trabajador 12", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 13
        self.fields['nombre_trab_13'] = forms.ChoiceField(label="Trabajador 13", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 14
        self.fields['nombre_trab_14'] = forms.ChoiceField(label="Trabajador 14", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 15
        self.fields['nombre_trab_15'] = forms.ChoiceField(label="Trabajador 15", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 16
        self.fields['nombre_trab_16'] = forms.ChoiceField(label="Trabajador 16", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 17
        self.fields['nombre_trab_17'] = forms.ChoiceField(label="Trabajador 17", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 18
        self.fields['nombre_trab_18'] = forms.ChoiceField(label="Trabajador 18", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 19
        self.fields['nombre_trab_19'] = forms.ChoiceField(label="Trabajador 19", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 20
        self.fields['nombre_trab_20'] = forms.ChoiceField(label="Trabajador 20", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 21
        self.fields['nombre_trab_21'] = forms.ChoiceField(label="Trabajador 21", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 22
        self.fields['nombre_trab_22'] = forms.ChoiceField(label="Trabajador 22", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 23
        self.fields['nombre_trab_23'] = forms.ChoiceField(label="Trabajador 23", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 24
        self.fields['nombre_trab_24'] = forms.ChoiceField(label="Trabajador 24", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 25
        self.fields['nombre_trab_25'] = forms.ChoiceField(label="Trabajador 25", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 26
        self.fields['nombre_trab_26'] = forms.ChoiceField(label="Trabajador 26", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 27
        self.fields['nombre_trab_27'] = forms.ChoiceField(label="Trabajador 27", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 28
        self.fields['nombre_trab_28'] = forms.ChoiceField(label="Trabajador 28", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 29
        self.fields['nombre_trab_29'] = forms.ChoiceField(label="Trabajador 29", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        # Trabajador 30
        self.fields['nombre_trab_30'] = forms.ChoiceField(label="Trabajador 30", widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        #---------------------------
        # Cargos de los trabajadores
        #---------------------------

        self.fields['cargo_trab_1'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_2'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_3'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_4'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_5'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_6'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_7'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_8'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_9'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_10'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_11'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_12'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_13'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_14'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_15'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_16'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_17'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_18'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_19'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_20'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_21'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_22'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_23'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_24'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_25'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_26'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_27'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_28'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_29'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

        self.fields['cargo_trab_30'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md form_style js-select2',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_cargos)

    autor = forms.CharField(label='Autor', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    mes = forms.ChoiceField(label='Mes', widget=Select(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = meses)

    ano = forms.ChoiceField(label='Año', widget=Select(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = anos)

    desc_avance = forms.CharField(label='Descripción general del avance del producto', widget=Textarea(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    obstaculos = forms.CharField(label='Dificultades y obstáculos', widget=Textarea(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'required': 'False',
    }), required = False)

    """
    nombre_trab_1 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_1 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_1 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_1 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_2 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_2 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_2 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_2 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_3 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_3 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_3 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_3 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_4 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_4 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_4 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_4 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_5 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_5 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_5 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_5 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_6 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_6 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_6 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_6 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_7 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_7 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_7 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_7 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_8 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_8 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_8 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_8 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_9 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_9 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_9 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_9 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_10 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_10 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_10 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_10 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_11 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_11 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_11 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_11 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_12 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_12 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_12 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_12 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_13 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_13 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_13 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_13 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_14 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_14 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_14 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_14 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_15 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_15 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_15 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_15 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_16 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_16 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_16 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_16 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_17 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_17 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_17 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_17 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_18 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_18 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_18 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_18 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_19 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_19 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_19 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_19 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_20 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_20 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_20 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_20 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_21 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_21 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_21 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_21 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_22 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_22 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_22 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_22 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_23 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_23 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_23 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_23 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_24 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_24 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_24 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_24 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_25 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_25 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_25 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_25 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_26 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_26 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_26 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_26 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_27 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_27 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_27 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_27 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_28 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_28 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_28 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_28 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_29 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_29 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_29 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_29 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    """
    nombre_trab_30 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)
    """

    act_asig_trab_30 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_30 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_30 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md form_style act',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    estatus = forms.ChoiceField(label='Estatus del reporte', widget=Select(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'False',
    }), choices = estatus_reportes_tareas)

    class Meta:

        model = Reporte
        fields = '__all__'
