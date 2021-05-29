# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indicadores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ano_beneficio', models.CharField(max_length=400, null=True, blank=True)),
                ('mes_beneficio', models.CharField(max_length=400, null=True, blank=True)),
                ('beneficio', models.CharField(max_length=400, null=True, blank=True)),
                ('cantidad', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('social', models.CharField(max_length=400, null=True, blank=True)),
                ('economico', models.CharField(max_length=400, null=True, blank=True)),
                ('productivo', models.CharField(max_length=400, null=True, blank=True)),
                ('ambiental', models.CharField(max_length=400, null=True, blank=True)),
                ('quienes', models.CharField(max_length=400, null=True, blank=True)),
                ('cuantos', models.PositiveIntegerField(default=0, null=True, blank=True)),
            ],
        ),
    ]
