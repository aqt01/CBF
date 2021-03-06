# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import newsletter.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=150, verbose_name='Correo')),
                ('is_active', models.EmailField(default=False, max_length=150, verbose_name='Correo')),
                ('activation_code', models.CharField(default=newsletter.utils.make_activation_code, max_length=40, verbose_name='activation code')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
