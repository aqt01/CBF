# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-11 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0007_auto_20170811_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliderimageextension',
            name='extended_object',
        ),
        migrations.RemoveField(
            model_name='sliderimageextension',
            name='public_extension',
        ),
    ]