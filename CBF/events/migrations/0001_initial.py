# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sermons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=150)),
                ('summary', models.CharField(verbose_name='Resumen', max_length=200, blank=True)),
                ('date_created', models.DateTimeField(verbose_name='Fecha de creacion', auto_now_add=True)),
                ('date_published', models.DateTimeField(verbose_name='Fecha de publicacion', auto_now_add=True)),
                ('is_published', models.BooleanField(verbose_name='Publicado?', default=True)),
                ('img', models.ImageField(verbose_name='Imagen del post', blank=True, upload_to='post_images')),
                ('start_date', models.DateTimeField(verbose_name='Fecha de inicio del evento')),
                ('end_date', models.DateTimeField(verbose_name='Fecha final del evento', blank=True)),
                ('location', models.TextField(verbose_name='Ubicacion del evento')),
                ('gmap_link', models.URLField(verbose_name='Link de Google Maps', blank=True, default='', help_text='Link externo de Googlemaps del evento')),
                ('tags', models.ManyToManyField(to='sermons.Tag')),
            ],
            options={
                'verbose_name': 'Eventos',
            },
        ),
    ]
