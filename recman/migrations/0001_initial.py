# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
                ('uom', models.CharField(default='oz', choices=[('oz', 'Ounces'), ('lbs', 'Pounds'), ('tps', 'Teaspoons'), ('tbs', 'Tablespoons'), ('cup', 'Cups'), ('wh', 'Whole'), ('clv', 'Cloves')], max_length=3)),
                ('qty', models.FloatField(default=0)),
                ('notes', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(default=None, choices=[('BREAKFAST', 'Breakfast'), ('ENTREE', 'Entree'), ('SOUP', 'Soups/Stews'), ('DESSERT', 'Dessert'), ('SNACK', 'Snack'), ('APPETIZER', 'Appetizer'), ('BEVERAGE', 'Beverage')], max_length=20)),
                ('subcategory', models.CharField(max_length=100)),
                ('prep_time', models.FloatField(max_length=4)),
                ('prep_time_uom', models.CharField(default='min', choices=[('min', 'Minutes'), ('hr', 'Hours')], max_length=3)),
                ('cook_time', models.FloatField(max_length=4)),
                ('cook_time_uom', models.CharField(default='min', choices=[('min', 'Minutes'), ('hr', 'Hours')], max_length=3)),
                ('instructions', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prep', models.CharField(blank=True, max_length=100)),
                ('qty', models.FloatField(default=0)),
                ('uom', models.CharField(default='oz', choices=[('oz', 'Ounces'), ('lbs', 'Pounds'), ('tps', 'Teaspoons'), ('tbs', 'Tablespoons'), ('cup', 'Cups'), ('wh', 'Whole'), ('clv', 'Cloves')], max_length=3)),
                ('optional', models.BooleanField()),
                ('notes', models.CharField(blank=True, max_length=200)),
                ('ingredient', models.ForeignKey(to='recman.Ingredient')),
                ('recipe', models.ForeignKey(to='recman.Recipe')),
            ],
        ),
    ]
