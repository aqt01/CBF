# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 20:19
from __future__ import unicode_literals

from django.db import migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sermons', '0003_auto_20170821_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sermon',
            name='content',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, max_length=1200, verbose_name='Contenido'),
        ),
    ]
