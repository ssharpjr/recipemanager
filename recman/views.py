from django.shortcuts import render, get_object_or_404, redirect

from .models import Recipe, Recipe_detail

from .forms import RecipeForm


def recipe_list(request):
	recipes = Recipe.objects.all().order_by('name')
	return render(request, 'recman/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
	recipe = get_object_or_404(Recipe, pk=pk)
	return render(request, 'recman/recipe_detail.html', {'recipe': recipe})

def recipe_new(request):
	if request.method == "POST":
		form = RecipeForm(request.POST)
		if form.is_valid():
			recipe = form.save()
			# Link any fields that are needed but not on the form (ie. User).
			recipe.save()
			return redirect('recman.views.recipe_detail', pk=recipe.pk)
	else:
		form = RecipeForm()
	return render(request, 'recman/recipe_edit.html', {'form': form})

def recipe_edit(request, pk):
	recipe = get_object_or_404(Recipe, pk=pk)
	if request.method == "POST":
		form = RecipeForm(request.POST, instance=recipe)
		if form.is_valid():
			recipe = form.save()
			# Link any fields that are needed but not on the form (ie. User).
			recipe.save()
			return redirect('recman.views.recipe_detail', pk=recipe.pk)
	else:
		form = RecipeForm(instance=recipe)
	return render(request, 'recman/recipe_edit.html', {'form': form})