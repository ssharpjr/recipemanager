# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recman', '0002_auto_20151006_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='uom',
            field=models.CharField(choices=[('oz', 'Ounces'), ('lbs', 'Pounds'), ('tps', 'Teaspoons'), ('tbs', 'Tablespoons'), ('cup', 'Cups'), ('whole', 'Whole'), ('clove', 'Cloves')], default='oz', max_length=4),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Entree', 'Entree'), ('Soup', 'Soups/Stews'), ('Dessert', 'Dessert'), ('Snack', 'Snack'), ('Appetizer', 'Appetizer'), ('Beverage', 'Beverage')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cook_time_uom',
            field=models.CharField(choices=[('mins', 'Minutes'), ('hr', 'Hours')], default='min', max_length=4),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time_uom',
            field=models.CharField(choices=[('mins', 'Minutes'), ('hr', 'Hours')], default='min', max_length=4),
        ),
        migrations.AlterField(
            model_name='recipe_detail',
            name='uom',
            field=models.CharField(choices=[('oz', 'Ounces'), ('lbs', 'Pounds'), ('tps', 'Teaspoons'), ('tbs', 'Tablespoons'), ('cup', 'Cups'), ('whole', 'Whole'), ('clove', 'Cloves')], default='oz', max_length=3),
        ),
    ]
