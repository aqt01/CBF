# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_member_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='img',
            field=models.ImageField(blank=True, default=1, upload_to='post_images', verbose_name='Imagen de perfil'),
            preserve_default=False,
        ),
    ]
