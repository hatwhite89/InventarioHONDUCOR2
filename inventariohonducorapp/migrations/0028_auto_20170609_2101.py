# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-10 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventariohonducorapp', '0027_auto_20170609_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_admin_inmueble',
            name='anio',
        ),
        migrations.AddField(
            model_name='tb_admin_inmueble',
            name='estado',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]