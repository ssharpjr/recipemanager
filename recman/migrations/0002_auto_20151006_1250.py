# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='uom',
            field=models.CharField(default='oz', max_length=4, choices=[('oz', 'Ounces'), ('lbs', 'Pounds'), ('tps', 'Teaspoons'), ('tbs', 'Tablespoons'), ('cup', 'Cups'), ('wh', 'Whole'), ('clv', 'Cloves')]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cook_time_uom',
            field=models.CharField(default='min', max_length=3, choices=[('mins', 'Minutes'), ('hr', 'Hours')]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time_uom',
            field=models.CharField(default='min', max_length=3, choices=[('mins', 'Minutes'), ('hr', 'Hours')]),
        ),
    ]
