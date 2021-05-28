# -*- coding: utf-8 -*-
from django import forms
from reportes.models import Indicadores
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField, NumberInput
)
from datetime import *
from django.contrib.admin.widgets import AdminDateWidget
from base.constantes import *

class IndicadoresForm(forms.ModelForm):
    """
    Formulario de los indicadores
    """

    """
    Apartado de los beneficios del proyecto
    """
    ano_beneficio = forms.ChoiceField(label='Año', widget=Select(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = anos)
    
    mes_beneficio = forms.ChoiceField(label='Mes', widget=Select(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), choices = meses)

    beneficio = forms.CharField(label='Beneficio', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    cantidad = forms.IntegerField(label='Cantidad', widget=NumberInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)


    """
    Apartado del impacto del proyecto
    """
    social = forms.CharField(label='Social', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    economico = forms.CharField(label='Económico', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    productivo = forms.CharField(label='Productivo', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    ambiental = forms.CharField(label='Ambiental', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)


    """
    Apartado para los beneficiarios del proyecto
    """
    quienes = forms.CharField(label='Quienes', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    cuantos = forms.CharField(label='Cuántos', widget=NumberInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    class Meta:
        
        model = Indicadores
        fields = '__all__'