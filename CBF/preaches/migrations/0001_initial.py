# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100)),
                ('telephone', models.CharField(max_length=12)),
                ('cellphone', models.CharField(max_length=12)),
                ('img', models.ImageField(upload_to='')),
                ('role', models.IntegerField(default=5, choices=[(0, 'Pastor titular'), (1, 'Pastor/a'), (2, 'Diacono/a'), (3, 'Editor/a')])),
            ],
        ),
        migrations.CreateModel(
            name='Preach',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('summary', models.CharField(blank=True, max_length=500)),
                ('date', models.DateField()),
                ('published_date', models.DateField(default=datetime.datetime(2017, 5, 7, 2, 3, 52, 71419))),
                ('url', models.URLField()),
                ('img', models.ImageField(verbose_name='Imagen', upload_to='images')),
                ('author', models.ForeignKey(to='preaches.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Social_media',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.IntegerField(default=0, verbose_name='Nombre de la red social', choices=[(0, 'Facebook'), (1, 'Instagram'), (2, 'Twitter')])),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Categoria', max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='preach',
            name='tags',
            field=models.ManyToManyField(to='preaches.Tags'),
        ),
        migrations.AddField(
            model_name='author',
            name='social_media',
            field=models.ManyToManyField(to='preaches.Social_media'),
        ),
    ]
