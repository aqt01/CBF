# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 04:04
from __future__ import unicode_literals

from django.db import migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0005_auto_20170828_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='content',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, max_length=2000, verbose_name='Contenido'),
        ),
    ]
