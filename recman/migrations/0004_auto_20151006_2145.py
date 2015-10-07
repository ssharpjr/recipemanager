# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recman', '0003_auto_20151006_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.FloatField(max_length=4, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.FloatField(max_length=4, blank=True),
        ),
    ]
