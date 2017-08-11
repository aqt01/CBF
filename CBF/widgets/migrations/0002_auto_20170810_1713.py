# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-10 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filer.fields.image
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('cms', '0016_auto_20160608_1535'),
        ('widgets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeBannerExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thought_banner_title', models.CharField(blank=True, max_length=150, verbose_name='Titulo en banner de reflexiones')),
                ('thought_banner_content', models.CharField(blank=True, max_length=150, verbose_name='Contenido en banner de reflexiones')),
                ('thought_banner', models.ImageField(blank=True, upload_to='banners')),
                ('sermon_banner_title', models.CharField(blank=True, max_length=150, verbose_name='Titulo en banner de sermones')),
                ('sermon_banner_content', models.CharField(blank=True, max_length=150, verbose_name='Contenido en banner de sermones')),
                ('sermon_banner', models.ImageField(blank=True, upload_to='banners')),
                ('followus_banner_title', models.CharField(blank=True, max_length=150, verbose_name='Titulo en banner de siguenos')),
                ('followus_banner_content', models.CharField(blank=True, max_length=150, verbose_name='Contenido en banner de siguenos')),
                ('followus_banner', models.ImageField(blank=True, upload_to='banners')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='widgets.HomeBannerExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrincipleExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Titulo en banner de reflexiones')),
                ('content', models.CharField(blank=True, max_length=150, verbose_name='Contenido en banner de reflexiones')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('icon', filer.fields.image.FilerImageField(blank=True, help_text='Tamaño sugerido: 1024x764', null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image', verbose_name='Imagen del banner')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='widgets.PrincipleExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SliderImageExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Titulo')),
                ('content', models.CharField(blank=True, max_length=150, verbose_name='Contenido')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('img', filer.fields.image.FilerImageField(blank=True, help_text='Tamaño sugerido: 1024x764', null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image', verbose_name='Imagen')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='widgets.SliderImageExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='sliderimage',
            name='extended_object',
        ),
        migrations.RemoveField(
            model_name='sliderimage',
            name='public_extension',
        ),
        migrations.RemoveField(
            model_name='bannerextension',
            name='followus_banner',
        ),
        migrations.RemoveField(
            model_name='bannerextension',
            name='followus_banner_text',
        ),
        migrations.RemoveField(
            model_name='bannerextension',
            name='followus_banner_title',
        ),
        migrations.RemoveField(
            model_name='bannerextension',
            name='sermon_banner',
        ),
        migrations.RemoveField(
            model_name='bannerextension',
            name='sermon_banner_text',
        ),
        migrations.RemoveField(
            model_name='bannerextension',
            name='sermon_banner_title',
        ),
        migrations.RemoveField(
            model_name='bannerextension',
            name='thought_banner',
        ),
        migrations.RemoveField(
            model_name='bannerextension',
            name='thought_banner_text',
        ),
        migrations.RemoveField(
            model_name='bannerextension',
            name='thought_banner_title',
        ),
        migrations.AddField(
            model_name='bannerextension',
            name='content',
            field=models.CharField(blank=True, max_length=150, verbose_name='Contenido'),
        ),
        migrations.AddField(
            model_name='bannerextension',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='bannerextension',
            name='img',
            field=filer.fields.image.FilerImageField(blank=True, help_text='Tamaño sugerido: 1024x764', null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='bannerextension',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='bannerextension',
            name='title',
            field=models.CharField(blank=True, max_length=150, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='sliderextension',
            name='slider',
            field=models.ManyToManyField(blank=True, to='widgets.SliderImageExtension'),
        ),
        migrations.DeleteModel(
            name='SliderImage',
        ),
    ]
