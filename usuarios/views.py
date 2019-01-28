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
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth import forms, login, logout, authenticate
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from .forms import LoginForm
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)


class LoginView(SuccessMessageMixin,FormView):
    """
    Clase que gestiona el formulario de inicio de
    sesión de los usuarios del sistema.
    """
    template_name = 'usuarios/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('inicio:index')
    success_message = "Bienvenido al sistema."

    def form_invalid(self, form):
        """
        Método que envía un mensaje al template del login cuando
        las credenciales de acceso no son válidos.
        """
        messages_alert = ['El usuario o la contraseña no son válidos.']
        return self.render_to_response(self.get_context_data(form=form,messages_alert=messages_alert))

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


def change_password(request):
    """
    Función que gestiona el cambio de contraseña
    de un usuario autenticado en el sistema.
    """
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages = ['Cambio de contraseña exitoso']
            return render_to_response("usuarios/change_password_done.html",{'messages':messages})
        else:
            print "No se realizó el cambio de contraseña"
    return render(request, 'usuarios/change_password.html', {'form': form})
