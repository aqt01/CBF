# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-14 20:42
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('name',))),
                ('publication_date', models.DateField(verbose_name='fecha de publicacion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen de la portada del libro')),
                ('author', models.CharField(blank=True, max_length=120, null=True)),
                ('book_url', models.URLField(verbose_name='Link de venta en Amazon')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
