from django.db import models

# TODO: (Model) Make this an editable list.
UOM_CHOICES = (
	('oz', 'Ounces'),
	('lbs', 'Pounds'),
	('tps', 'Teaspoons'),
	('tbs', 'Tablespoons'),
	('cup', 'Cups'),
	('wh', 'Whole'),
	('clv', 'Cloves'),
	)

TIME_UOM_CHOICES = (
	('min', 'Minutes'),
	('hr', 'Hours'),
	)

# TODO: (Model) Make this an editable list.
CAT_CHOICES = (
	('BREAKFAST',	'Breakfast'),
	('ENTREE', 		'Entree'),
	('SOUP',   		'Soups/Stews'),
	('DESSERT',		'Dessert'),
	('SNACK',		'Snack'),
	('APPETIZER',	'Appetizer'),
	('BEVERAGE',	'Beverage')
	)



class Meal(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
        category = models.CharField(max_length=20,
									choices=CAT_CHOICES,
									default=None)
	notes = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name



class Recipe(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
		subcategory = models.CharField(max_length=100)
	prep_time = models.FloatField(max_length=4)
	uom = models.CharField(max_length=3,
							choices=UOM_CHOICES,
							default='oz')
	qty = models.FloatField(default=0)
	prep_time_uom = models.CharField(max_length=3,
									choices=TIME_UOM_CHOICES,
									default='min')
	cook_time = models.FloatField(max_length=4)
	cook_time_uom = models.CharField(max_length=3,
									choices=TIME_UOM_CHOICES,
									default='min')
	instructions = models.TextField(blank=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		return self.name


class RecipeIngredient(models.Model):
	recipe = models.ForeignKey(Recipe)
        ingredient = models.ForeignKey(Ingredient)
	qty = models.FloatField(default=0)
	uom = models.CharField(max_length=3,
							choices=UOM_CHOICES,
							default='oz')
	optional = models.BooleanField()
	notes = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.ingredient.name