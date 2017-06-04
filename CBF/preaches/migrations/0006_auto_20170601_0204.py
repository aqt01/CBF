# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('preaches', '0005_auto_20170525_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='social_media',
        ),
        migrations.RemoveField(
            model_name='preach',
            name='date',
        ),
        migrations.RemoveField(
            model_name='preach',
            name='published_date',
        ),
        migrations.AddField(
            model_name='preach',
            name='content',
            field=models.TextField(verbose_name='Texto', blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='preach',
            name='date_created',
            field=models.DateField(verbose_name='Fecha', default=datetime.datetime(2017, 6, 1, 6, 4, 33, 855133, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preach',
            name='date_published',
            field=models.DateField(verbose_name='Fecha de publicacion', default=datetime.datetime(2017, 6, 1, 2, 4, 18, 846168)),
        ),
        migrations.AddField(
            model_name='preach',
            name='is_published',
            field=models.BooleanField(verbose_name='Publicado?', default=True),
        ),
        migrations.AddField(
            model_name='social_media',
            name='author',
            field=models.ForeignKey(to='preaches.Author', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='cellphone',
            field=models.CharField(verbose_name='Numero de celular', max_length=12),
        ),
        migrations.AlterField(
            model_name='author',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Imagen de perfil', help_text='Tamaño sugerido 36x36'),
        ),
        migrations.AlterField(
            model_name='author',
            name='role',
            field=models.IntegerField(choices=[(0, 'Pastor titular'), (1, 'Pastor'), (2, 'Pastora'), (3, 'Diacono'), (4, 'Diacona'), (5, 'Editor'), (6, 'Editora')], verbose_name='Rol', default=5),
        ),
        migrations.AlterField(
            model_name='author',
            name='telephone',
            field=models.CharField(verbose_name='Numero de telefono', max_length=12),
        ),
        migrations.AlterField(
            model_name='preach',
            name='summary',
            field=models.TextField(verbose_name='Resumen', blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='preach',
            name='title',
            field=models.CharField(verbose_name='Titulo de la predica', max_length=60),
        ),
    ]
