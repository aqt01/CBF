# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-14 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filer.fields.image
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo electronico')),
                ('telephone', models.CharField(blank=True, max_length=12, verbose_name='Numero de telefono')),
                ('cellphone', models.CharField(blank=True, max_length=12, verbose_name='Numero de celular')),
                ('role', models.IntegerField(blank=True, choices=[(0, 'Pastor titular'), (1, 'Pastor'), (2, 'Pastora'), (3, 'Diacono'), (4, 'Diacona'), (5, 'Editor'), (6, 'Editora'), (7, 'Miembro')], default=5, verbose_name='Rol')),
                ('profile_img', filer.fields.image.FilerImageField(blank=True, help_text='Tamaño sugerido: 50x50', null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image', verbose_name='Imagen de perfil')),
            ],
            options={
                'verbose_name': 'Miembro',
                'verbose_name_plural': 'Miembros',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.IntegerField(choices=[(0, 'Facebook'), (1, 'Instagram'), (2, 'Twitter')], default=0, verbose_name='Nombre de la red social')),
                ('url', models.URLField(verbose_name='Link de la red social')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.Member')),
            ],
            options={
                'verbose_name': 'Red social',
                'verbose_name_plural': 'Redes sociales',
            },
        ),
    ]
