# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms import (
    ModelForm, TextInput, EmailInput, CharField, EmailField, PasswordInput, Select, CheckboxInput
)
from django import forms
from base.constantes import *


class LoginForm(AuthenticationForm):
    """
    Clase que gestiona los campos del formulario de
    inicio de sesión de usuarios del sistema.
    """
    username = forms.CharField(widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 15%; display: inline;',
    }), required = True)

    password = forms.CharField(widget=PasswordInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 15%; display: inline;',
    }), required = True)

    class Meta:
        model = User

    fields = [
        'username',
        'password',
    ]


class MyRegistrationForm(UserCreationForm):
    """
    Clase que gestiona el formulario para el registro de usuarios del sistema.
    """
    username = forms.CharField(label='Nombre de usuario',widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'tabindex': '1'
    }), required = True)

    password1 = forms.CharField(label='Contraseña',widget=PasswordInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'tabindex': '5'
    }), required = True)

    password2 = forms.CharField(label='Confirmar contraseña',widget=PasswordInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'tabindex': '6'
    }), required = True)

    first_name = forms.CharField(label='Primer nombre',widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'tabindex': '3'
    }), required = True)

    last_name = forms.CharField(label='Primer apellido',widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'tabindex': '4'
    }), required = True)

    email = forms.EmailField(label='Correo electrónico',widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'tabindex': '2'
    }), required = True)

    """
    is_active = forms.BooleanField(label='Cara visible',widget=CheckboxInput(attrs={
        'class':'checkbox',
    }), required = False)

    is_staff = forms.BooleanField(label='Director',widget=CheckboxInput(attrs={
        'class':'checkbox',
    }), required = False)

    is_superuser = forms.BooleanField(label='Analista',widget=CheckboxInput(attrs={
        'class':'checkbox',
    }), required = False)
    """
    rol = forms.ChoiceField(label='Rol', widget=Select(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), choices=usuarios,required=False)

    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name','email','rol')


class UserForm(forms.ModelForm):
    """
    Clase del formulario que permite actualizar la información de los usuarios del sistema.
    """
    username = forms.CharField(label='Nombre de usuario',widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'tabindex': '1'
    }), required = True)

    first_name = forms.CharField(label='Primer nombre',widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'tabindex': '3'
    }), required = True)

    last_name = forms.CharField(label='Primer apellido',widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'tabindex': '4'
    }), required = True)

    email = forms.EmailField(label='Correo electrónico',widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'tabindex': '2'
    }), required = True)

    is_active = forms.BooleanField(label='Administrador',widget=CheckboxInput(attrs={
        'class':'checkbox',
    }), required = False)

    is_staff = forms.BooleanField(label='Analista de servicios',widget=CheckboxInput(attrs={
        'class':'checkbox',
    }), required = False)

    is_superuser = forms.BooleanField(label='Administrador',widget=CheckboxInput(attrs={
        'class':'checkbox',
    }), required = False)

    rol = forms.ChoiceField(label='Rol', widget=Select(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), choices=usuarios,required = False)

    class Meta:
        model = User
        exclude = ('password1','password2')
        fields = ('username','first_name','last_name','email','rol','is_active','is_staff','is_superuser')
