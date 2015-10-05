from django.shortcuts import render

from .models import Recipe


def recipe_list(request):
	recipes = Recipe.objects.all().order_by('name')
	return render(request, 'recman/recipe_list.html', {'recipes': recipes})

