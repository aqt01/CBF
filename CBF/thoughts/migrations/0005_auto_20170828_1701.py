# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 21:01
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0004_auto_20170828_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique_with=('name',)),
        ),
    ]
