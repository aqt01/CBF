# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0002_auto_20170821_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principle',
            name='content',
            field=models.CharField(blank=True, max_length=800, verbose_name='Contenido'),
        ),
    ]
