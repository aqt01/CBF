# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('preaches', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.AlterField(
            model_name='preach',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2017, 5, 25, 15, 58, 42, 206921)),
        ),
    ]
