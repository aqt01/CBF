# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-11 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0011_auto_20170811_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='extended_object',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='public_extension',
        ),
    ]
