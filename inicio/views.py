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
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)


class Index(TemplateView):
    """
    Plantilla de inicio del sistema
    """
    template_name = "inicio/index.html"
