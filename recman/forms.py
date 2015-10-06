from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
	
	class Meta:
		model = Recipe
		fields = ('name', 'description', 'category', 'subcategory',
					'prep_time', 'prep_time_uom', 'cook_time', 'cook_time_uom',
					'instructions', 'notes')