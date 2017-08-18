# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-14 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filer.fields.image
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0001_initial'),
        ('filer', '0007_auto_20161016_1055'),
        ('sermons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('summary', models.CharField(blank=True, max_length=200, verbose_name='Resumen')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicacion')),
                ('is_published', models.BooleanField(default=True, verbose_name='Publicado?')),
                ('date_created', models.DateTimeField(verbose_name='Fecha de creacion')),
                ('content', models.TextField(blank=True, max_length=1200, verbose_name='Contenido')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membership.Member')),
                ('img', filer.fields.image.FilerImageField(blank=True, help_text='Tamaño sugerido: 1024x765', null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image', verbose_name='Imagen del post')),
                ('tags', models.ManyToManyField(blank=True, to='sermons.Tag')),
            ],
            options={
                'verbose_name': 'Reflexion',
                'verbose_name_plural': 'Reflexiones',
            },
        ),
    ]
