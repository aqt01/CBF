# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_member_role_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role_description',
            field=models.CharField(blank=True, max_length=150, verbose_name='Descripcion del rol'),
        ),
    ]
