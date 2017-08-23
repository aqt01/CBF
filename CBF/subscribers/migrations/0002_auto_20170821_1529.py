# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-21 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=150, unique=True, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='is_active',
            field=models.BooleanField(default=False, max_length=150, verbose_name='Email confirmado?'),
        ),
    ]