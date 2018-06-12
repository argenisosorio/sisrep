# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, RedirectView, CreateView, UpdateView, ListView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, logout, authenticate
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import LoginForm


class LoginView(FormView):
    """
    Clase que gestiona el formulario de inicio de
    sesión de los usuarios del sistema.
    """
    template_name = 'usuarios/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('registro:index')

    def form_valid(self, form):
        """
        Método que valida si la data enviada en el
        formulario es válida para el inicio de sesión.
        """
        usuario = form.cleaned_data['username']
        contrasena = form.cleaned_data['password']
        usuario = authenticate(username=usuario, password=contrasena)
        login(self.request, usuario)
        return super(LoginView, self).form_valid(form)


class Logout(View):
    """
    Clase que gestiona el cierre de sesión
    de los usuarios del sistema.
    """

    def get(self, request):
        """
        Método que cierra la sesión del usuario
        y redirecciona al formulario de inicio
        de sesión.
        """
        logout(request)
        return redirect('usuarios:login')
