# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventariohonducorapp', '0051_tb_empleado_puesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_vehiculo',
            name='agencia',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
