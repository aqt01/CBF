# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 04:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170808_0210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-start_date'], 'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
    ]