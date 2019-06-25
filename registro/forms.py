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
        'class':'form-control input-md',
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
    nombre_caravisible = forms.CharField(label='Nombre del cara visible', widget=TextInput(attrs={
        'class':'form-control input-md',
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
        'class':'form-control input-md',
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
        'class':'form-control input-md',
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
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_proyectos)

        self.fields['nombre_caravisible'] = forms.ChoiceField(label="Cara visible", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_caravisibles)

        self.fields['nombre_director'] = forms.ChoiceField(label="Director", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_directores)

        self.fields['cargo_trab_1'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices = lista_cargos, required = False)
        
        self.fields['cargo_trab_2'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices = lista_cargos, required = False)
        
        self.fields['cargo_trab_3'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices = lista_cargos, required = False)
        
        self.fields['cargo_trab_4'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices = lista_cargos, required = False)
        
        self.fields['cargo_trab_5'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices = lista_cargos, required = False)
        
        self.fields['cargo_trab_6'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices = lista_cargos, required = False)
        
        self.fields['cargo_trab_7'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices = lista_cargos, required = False)
        
        self.fields['cargo_trab_8'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices = lista_cargos, required = False)
        
        self.fields['cargo_trab_9'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices = lista_cargos, required = False)
        
        self.fields['cargo_trab_10'] = forms.ChoiceField(label='Cargo', widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices = lista_cargos, required = False)

    autor = forms.CharField(label='Autor', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

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

    desc_avance = forms.CharField(label='Descripción general del avance del producto', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    obstaculos = forms.CharField(label='Dificultades y obstáculos', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    nombre_trab_1 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_asig_trab_1 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

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

    act_asig_trab_2 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

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

    act_asig_trab_3 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_3 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_3 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_trab_4 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_asig_trab_4 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_4 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_4 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_trab_5 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_asig_trab_5 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_5 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_5 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_trab_6 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_asig_trab_6 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_6 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_6 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_trab_7 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_asig_trab_7 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_7 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_7 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_trab_8 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_asig_trab_8 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_8 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_8 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_trab_9 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_asig_trab_9 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_9 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_9 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_trab_10 = forms.CharField(label='Nombre del trabajador', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_asig_trab_10 = forms.CharField(label='Actividades asignadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    act_rea_trab_10 = forms.CharField(label='Actividades realizadas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    enlaces_trab_10 = forms.CharField(label='Enlaces de verificación', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    class Meta:

        model = Reporte
        fields = '__all__'