# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 04:55
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('membership', '0005_auto_20170809_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='img',
        ),
        migrations.AddField(
            model_name='member',
            name='profile_img',
            field=filer.fields.image.FilerImageField(blank=True, help_text='Tamaño sugerido: 50x50', null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image', verbose_name='Imagen de perfil'),
        ),
    ]
