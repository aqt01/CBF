# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-08 06:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
    ]
