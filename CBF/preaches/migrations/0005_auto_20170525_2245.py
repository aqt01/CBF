# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('preaches', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preach',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2017, 5, 25, 22, 45, 15, 574720)),
        ),
    ]
