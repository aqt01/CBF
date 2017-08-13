# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-11 06:36
from __future__ import unicode_literals

from django.db import migrations
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0003_principlegroupextension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principleextension',
            name='icon',
            field=fontawesome.fields.IconField(blank=True, default=1, max_length=60),
            preserve_default=False,
        ),
    ]