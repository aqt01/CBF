# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-22 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170821_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion'),
        ),
    ]
