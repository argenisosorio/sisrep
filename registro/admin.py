# -*- coding: utf-8 -*-
from django.contrib import admin
from registro.models import Reporte, Proyecto, Caravisible, Director


admin.site.register(Proyecto)
admin.site.register(Caravisible)
admin.site.register(Director)
admin.site.register(Reporte)