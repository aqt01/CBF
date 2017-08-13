# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-10 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thought_banner_title', models.CharField(blank=True, max_length=150, verbose_name='Titulo en banner de reflexiones')),
                ('thought_banner_text', models.CharField(blank=True, max_length=150, verbose_name='Texto en banner de reflexiones')),
                ('thought_banner', models.ImageField(blank=True, upload_to='banners')),
                ('sermon_banner_title', models.CharField(blank=True, max_length=150, verbose_name='Titulo en banner de sermones')),
                ('sermon_banner_text', models.CharField(blank=True, max_length=150, verbose_name='Texto en banner de sermones')),
                ('sermon_banner', models.ImageField(blank=True, upload_to='banners')),
                ('followus_banner_title', models.CharField(blank=True, max_length=150, verbose_name='Titulo en banner de siguenos')),
                ('followus_banner_text', models.CharField(blank=True, max_length=150, verbose_name='Texto en banner de siguenos')),
                ('followus_banner', models.ImageField(blank=True, upload_to='banners')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='widgets.BannerExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SliderExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='widgets.SliderExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Titulo del slide')),
                ('sub_name', models.CharField(blank=True, max_length=150, verbose_name='Subtitulo del slide')),
                ('img', models.ImageField(blank=True, upload_to='slide_images', verbose_name='Imagen del slide')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='widgets.SliderImage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='sliderextension',
            name='slider',
            field=models.ManyToManyField(blank=True, to='widgets.SliderImage'),
        ),
    ]