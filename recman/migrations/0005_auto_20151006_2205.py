# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recman', '0004_auto_20151006_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='uom',
            field=models.CharField(default='oz', choices=[('oz', 'Ounces'), ('lbs', 'Pounds'), ('tps', 'Teaspoons'), ('tbs', 'Tablespoons'), ('cup', 'Cups'), ('whole', 'Whole'), ('each', 'each'), ('clove', 'Cloves')], max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe_detail',
            name='uom',
            field=models.CharField(default='oz', choices=[('oz', 'Ounces'), ('lbs', 'Pounds'), ('tps', 'Teaspoons'), ('tbs', 'Tablespoons'), ('cup', 'Cups'), ('whole', 'Whole'), ('each', 'each'), ('clove', 'Cloves')], max_length=3),
        ),
    ]
