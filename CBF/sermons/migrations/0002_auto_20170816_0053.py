# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-16 04:53
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sermons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sermon',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='name', unique_with=('name',)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sermon',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]