# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 05:01
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20170809_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='img',
            field=filer.fields.image.FilerImageField(blank=True, help_text='Tamaño sugerido: 1024x765', null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image', verbose_name='Imagen del post'),
        ),
    ]
