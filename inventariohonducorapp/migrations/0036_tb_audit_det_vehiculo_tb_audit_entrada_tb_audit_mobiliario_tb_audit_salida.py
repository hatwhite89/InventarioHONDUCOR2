# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-10 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventariohonducorapp', '0035_tb_audit_det_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_audit_det_vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TableName', models.CharField(max_length=45)),
                ('Operation', models.CharField(max_length=1)),
                ('OldValue', models.TextField(blank=True, null=True)),
                ('NewValue', models.TextField(blank=True, null=True)),
                ('UpdateDate', models.DateField()),
                ('UserName', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='tb_audit_entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TableName', models.CharField(max_length=45)),
                ('Operation', models.CharField(max_length=1)),
                ('OldValue', models.TextField(blank=True, null=True)),
                ('NewValue', models.TextField(blank=True, null=True)),
                ('UpdateDate', models.DateField()),
                ('UserName', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='tb_audit_mobiliario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TableName', models.CharField(max_length=45)),
                ('Operation', models.CharField(max_length=1)),
                ('OldValue', models.TextField(blank=True, null=True)),
                ('NewValue', models.TextField(blank=True, null=True)),
                ('UpdateDate', models.DateField()),
                ('UserName', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='tb_audit_salida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TableName', models.CharField(max_length=45)),
                ('Operation', models.CharField(max_length=1)),
                ('OldValue', models.TextField(blank=True, null=True)),
                ('NewValue', models.TextField(blank=True, null=True)),
                ('UpdateDate', models.DateField()),
                ('UserName', models.CharField(max_length=45)),
            ],
        ),
    ]
