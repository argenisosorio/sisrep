# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, RedirectView, CreateView, UpdateView, ListView, TemplateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from .models import *
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth import forms, login, logout, authenticate
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import LoginForm, MyRegistrationForm, UserForm
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, AdminPasswordChangeForm
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


class ListUsers(ListView):
    """
    Clase que permite consultar la lista de usuarios.
    """
    model = User
    template_name = "usuarios/list_users.html"

    def get(self, request, *args, **kwargs):
        """
        Método que valida si el usuario es admin para ver la lista de objetos.
        """
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            if (self.get_paginate_by(self.object_list) is not None
                    and hasattr(self.object_list, 'exists')):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
                        % {'class_name': self.__class__.__name__})
        context = self.get_context_data()
        if request.user.is_superuser:
            return self.render_to_response(context)
        else:
            messages_alert = ['No tiene permisos para listar los usuarios del sistema']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class RegisterUser(CreateView):
    """
    Clase que gestiona el formulario registro de usuarios del sistema.
    """
    model = User
    template_name = "usuarios/register.html"
    form_class = MyRegistrationForm
    success_url = reverse_lazy('usuarios:list_users')
    success_message = "Se registró el usuario con éxito"

    def get(self, request, *args, **kwargs):
        """
        Méroto que valida si el usuario autenticado es admin
        para poder registrar un usuario.
        """
        self.object = None
        if request.user.is_superuser:
            return super(RegisterUser, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para registrar un usuario']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))

    def form_valid(self, form):
        """
        Método gestiona la validación de los datos enviados en el
        formulario y envía un mensaje de confirmación.
        """
        self.object = form.save(commit=False)
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.password1 = form.cleaned_data['password1']
        self.object.password2 = form.cleaned_data['password2']
        self.object.is_staff = form.cleaned_data['is_staff']
        self.object.is_active = form.cleaned_data['is_active']
        self.object.is_superuser = form.cleaned_data['is_superuser']
        self.object.save()
        messages.success(self.request, self.success_message)
        return super(RegisterUser, self).form_valid(form)


class EditUser(SuccessMessageMixin, UpdateView):
    """
    Clase que gestiona la actualización de los datos de un usuario.
    """
    model = User
    template_name = "usuarios/edit_user.html"
    form_class = UserForm
    success_message = "Usuario actualizado con éxito"
    success_url = reverse_lazy('usuarios:list_users')

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar el usuario no es admin.
        """
        if request.user.is_superuser:
            return super(EditUser, self).get(request, *args, **kwargs)
        else:
            messages_alert = ['No tiene permisos para editar el usuario']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class DeleteUser(SuccessMessageMixin, DeleteView):
    """
    Clase que permite borrar un proyecto poa.
    """
    model = User
    success_url = reverse_lazy('usuarios:list_users')
    template_name = "usuarios/user_confirm_delete.html"
    success_message = "Se elimino el usuario con éxito"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteUser, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta borrar el usuario no es admin.
        """
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if request.user.is_superuser:
            return self.render_to_response(context)
        else:
            messages_alert = ['No tiene permisos para borrar el usuario']
            return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


def user_change_password(request,pk):
    """
    Función que gestiona la actualización de las contraseña de un usuario.
    """
    model = User
    usuario = get_object_or_404(User, pk=pk)
    print usuario
    form = AdminPasswordChangeForm(user=usuario)
    if request.method == 'POST':
        form = AdminPasswordChangeForm(user=usuario, data=request.POST)
        if form.is_valid():
            form.save()
            #messages = ['Se actualizó la contraseña del usuario con éxito']
            #return render_to_response("inicio/index.html",{'messages':messages},context_instance=RequestContext(request))
            return redirect('usuarios:list_users')
        else:
            print "No se realizó el cambio de contraseña"
    return render(request, 'usuarios/user_change_password.html',{'form':form,'usuario':usuario})
