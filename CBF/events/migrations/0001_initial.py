# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre del evento', max_length=60)),
                ('summary', models.CharField(verbose_name='Resumen del evento', max_length=500, blank=True)),
                ('start_date', models.DateTimeField(verbose_name='Fecha de inicio del evento')),
                ('end_date', models.DateTimeField(verbose_name='Fecha final del evento', blank=True)),
                ('img', models.ImageField(verbose_name='Imagen del evento', upload_to='')),
                ('location', models.TextField(verbose_name='Ubicacion del evento')),
                ('gmap_link', models.URLField(verbose_name='Link de Google Maps', help_text='Link externo de Googlemaps del evento', default='', blank=True)),
            ],
        ),
    ]
