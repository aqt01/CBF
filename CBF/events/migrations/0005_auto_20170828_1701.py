# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 21:01
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20170821_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='content',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, max_length=1200, verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique_with=('name',)),
        ),
    ]
