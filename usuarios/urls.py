# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from usuarios import views
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name = "login"),
    url(r'logout/$', views.Logout.as_view(), name='logout'),
    url(r'^register$', views.RegisterUser.as_view(), name='register'),
    url(r'^list_users/$', login_required(views.ListUsers.as_view()), name='list_users'),
    url(r'^cambiar-contrasena/$', login_required(views.change_password), name='change_password'),
    url(r'^edit_user/(?P<pk>\d+)$', login_required(views.EditUser.as_view()), name='edit_user'),
    url(r'^delete_user/(?P<pk>\d+)$', login_required(views.DeleteUser.as_view()), name='delete_user'),
    url(r'^user_change_password/(?P<pk>\d+)$', login_required(views.user_change_password), name='user_change_password'),
)
