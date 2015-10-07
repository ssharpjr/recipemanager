from django.db import models

# TODO: (Model) Make this an editable list.
UOM_CHOICES = (
	('oz', 'Ounces'),
	('lbs', 'Pounds'),
	('tps', 'Teaspoons'),
	('tbs', 'Tablespoons'),
	('cup', 'Cups'),
	('whole', 'Whole'),
	('each', 'Each'),
	('clove', 'Cloves'),
	('can', 'Can'),
	)

TIME_UOM_CHOICES = (
	('mins', 'Minutes'),
	('hr', 'Hours'),
	)

# TODO: (Model) Make this an editable list.
CAT_CHOICES = (
	('Breakfast',	'Breakfast'),
	('Entree', 		'Entree'),
	('Soup',   		'Soups/Stews'),
	('Dessert',		'Dessert'),
	('Snack',		'Snack'),
	('Appetizer',	'Appetizer'),
	('Beverage',	'Beverage')
	)



class Ingredient(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	subcategory = models.CharField(max_length=100)
	uom = models.CharField(max_length=20,
							choices=UOM_CHOICES,
							default='oz')
	qty = models.FloatField(default=0)
	notes = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name



class Recipe(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	category = models.CharField(max_length=20,
									choices=CAT_CHOICES,
									default=None)
	subcategory = models.CharField(max_length=100)
	prep_time = models.FloatField(max_length=4, blank=True)
	prep_time_uom = models.CharField(max_length=4,
									choices=TIME_UOM_CHOICES,
									default='min')
	cook_time = models.FloatField(max_length=4, blank=True)
	cook_time_uom = models.CharField(max_length=4,
									choices=TIME_UOM_CHOICES,
									default='min')
	instructions = models.TextField(blank=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		return self.name

	def ready_in(self):
		prep_time_min = 0
		cook_time_min = 0
		time_uom = 'min'
		hours = 0
		minutes = 0

		# Convert hours to minutes
		if self.prep_time_uom == 'hr':
			prep_time_min = self.prep_time * 60
		else:
			prep_time_min = self.prep_time
		if self.cook_time_uom == 'hr':
			cook_time_min = self.cook_time * 60
		else:
			cook_time_min = self.cook_time
		total_time = prep_time_min + cook_time_min
		# Convert to the most reasonable time
		if total_time >= 60:
			# If gt 1 hour, use hours and minutes
			time_uom = 'hrs'
			hours = total_time // 60
			minutes = total_time % 60
			if hours == 1:
				time_uom = 'hr'
		else:
			time_uom = 'mins'
		# Build the output
		if time_uom == 'hr' or 'hrs':
			time_output = str("{:g}".format(hours)) + ' ' + time_uom + \
				', ' + str("{:g}". format(minutes)) + ' mins'
		else:
			time_output = str("{:g}".format(minutes)) + ' ' + time_uom
		return time_output



class Recipe_detail(models.Model):
	recipe = models.ForeignKey(Recipe)
	ingredient = models.ForeignKey(Ingredient)
	prep = models.CharField(max_length=100, blank=True)
	qty = models.FloatField(default=0)
	uom = models.CharField(max_length=20,
							choices=UOM_CHOICES,
							default='each')
	optional = models.BooleanField()
	notes = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.ingredient.name