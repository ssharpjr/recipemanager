# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recman', '0006_auto_20151006_2211'),
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
        migrations.AlterField(
            model_name='recipe_detail',
            name='uom',
            field=models.CharField(max_length=20, choices=[('oz', 'Ounces'), ('lbs', 'Pounds'), ('tps', 'Teaspoons'), ('tbs', 'Tablespoons'), ('cup', 'Cups'), ('whole', 'Whole'), ('each', 'Each'), ('clove', 'Cloves'), ('can', 'Can')], default='each'),
        ),
    ]
