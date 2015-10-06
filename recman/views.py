from django.shortcuts import render, get_object_or_404

from .models import Recipe, Recipe_detail

from .forms import RecipeForm


def recipe_list(request):
	recipes = Recipe.objects.all().order_by('name')
	return render(request, 'recman/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
	recipe = get_object_or_404(Recipe, pk=pk)
	ready_in = recipe.prep_time + recipe.cook_time
	return render(request, 'recman/recipe_detail.html', {'recipe': recipe})

def recipe_new(request):
	form = RecipeForm()
	return render(request, 'recman/recipe_edit.html', {'form': form})

