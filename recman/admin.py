from django.contrib import admin

from .models import Recipe, Recipe_detail, Ingredient



class IngredientInline(admin.TabularInline):
	model = Recipe_detail
	verbose_name = "Ingredient"
	verbose_name_plural = "Ingredients"
	extra = 1



class RecipeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 					{'fields': ['name']}),
		('Details',				{'fields': ['description', ('category', 'subcategory')]}),
		('Prep & Cook Times',	{'fields': [('prep_time', 'prep_time_uom'), 
											('cook_time', 'cook_time_uom'),]}),
		('Instructions',		{'fields': ['instructions', 'notes']})
	]

	inlines = [IngredientInline]

	list_display = ('name', 'description', 'category', 'subcategory')
	list_filter = ['category', 'subcategory']
	search_fields = ['name']



class IngredientAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'qty', 'uom', 'category')
	list_filter  = ['category', 'uom']
	search_fields = ['name']



admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)