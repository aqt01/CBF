# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-10 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('widgets', '0002_auto_20170810_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrincipleGroupExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('principles', models.ManyToManyField(blank=True, to='widgets.PrincipleExtension')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='widgets.PrincipleGroupExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
