# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from usuarios import views
from .views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns=patterns('',
    url(r'^login/$',LoginView.as_view(),name="login"),
    url(r'logout/$',views.Logout.as_view(),name='logout'),
    url(r'^register$',views.RegisterUser.as_view(),name='register'),
    url(r'^list_users/$',login_required(views.ListUsers.as_view()),name='list_users'),
    url(r'^cambiar-contrasena/$',login_required(views.change_password),name='change_password'),
    url(r'^edit_user/(?P<pk>\d+)$',login_required(views.EditUser.as_view()),name='edit_user'),
    url(r'^delete_user/(?P<pk>\d+)$',login_required(views.DeleteUser.as_view()),name='delete_user'),
    url(r'^user_change_password/(?P<pk>\d+)$',login_required(views.user_change_password),name='user_change_password'),
    # Urls para el restablecimiento de contraseña por correo.
    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset',
        {'post_reset_redirect':'passwordsent/','template_name':'usuarios/password_reset_form.html',
        'email_template_name':'usuarios/password_reset_email.html'},name='password_reset'),
    url(r'^resetpassword/passwordsent/$','django.contrib.auth.views.password_reset_done',
        {'template_name':'usuarios/password_reset_done.html'},name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect':reverse_lazy('usuarios:password_reset_complete'),'template_name':'usuarios/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset/done/$','django.contrib.auth.views.password_reset_complete',
        {'template_name':'usuarios/password_reset_complete.html'},
        name='password_reset_complete'),
)
