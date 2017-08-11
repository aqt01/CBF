# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=150)),
                ('summary', models.CharField(verbose_name='Resumen', max_length=200, blank=True)),
                ('date_created', models.DateTimeField(verbose_name='Fecha de creacion', auto_now_add=True)),
                ('date_published', models.DateTimeField(verbose_name='Fecha de publicacion', auto_now_add=True)),
                ('is_published', models.BooleanField(verbose_name='Publicado?', default=True)),
                ('img', models.ImageField(verbose_name='Imagen del post', blank=True, upload_to='post_images')),
                ('telephone', models.CharField(verbose_name='Numero de telefono', max_length=12)),
                ('cellphone', models.CharField(verbose_name='Numero de celular', max_length=12)),
                ('role', models.IntegerField(verbose_name='Rol', default=5, choices=[(0, 'Pastor titular'), (1, 'Pastor'), (2, 'Pastora'), (3, 'Diacono'), (4, 'Diacona'), (5, 'Editor'), (6, 'Editora')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=150)),
                ('summary', models.CharField(verbose_name='Resumen', max_length=200, blank=True)),
                ('date_created', models.DateTimeField(verbose_name='Fecha de creacion', auto_now_add=True)),
                ('date_published', models.DateTimeField(verbose_name='Fecha de publicacion', auto_now_add=True)),
                ('is_published', models.BooleanField(verbose_name='Publicado?', default=True)),
                ('img', models.ImageField(verbose_name='Imagen del post', blank=True, upload_to='post_images')),
                ('content', models.TextField(verbose_name='Contenido', max_length=1200, blank=True)),
                ('url', models.URLField(max_length=250)),
                ('author', models.ForeignKey(blank=True, null=True, to='sermons.Author')),
            ],
            options={
                'verbose_name': 'Sermones',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.IntegerField(verbose_name='Nombre de la red social', default=0, choices=[(0, 'Facebook'), (1, 'Instagram'), (2, 'Twitter')])),
                ('url', models.URLField()),
                ('author', models.ForeignKey(to='sermons.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Categoria', max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='sermon',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='sermons.Tag'),
        ),
    ]
