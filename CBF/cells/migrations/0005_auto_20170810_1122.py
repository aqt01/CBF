# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-10 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cells', '0004_cell_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cell',
            old_name='author',
            new_name='incharge',
        ),
    ]
