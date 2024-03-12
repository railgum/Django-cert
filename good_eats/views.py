from django.shortcuts import render, HttpResponse, Http404, get_object_or_404
from random import choice
from .models import *


def index(request):
    recipes = Recipe.objects.all()
    recipes_for_index = []
    for _ in range(1, 7):
        recipes_for_index.append(choice(recipes))
    context = {
        'title': 'Главная',
        'recipes': recipes_for_index,
    }
    return render(request, 'good_eats/index.html', context)


def single_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {
        'title': 'Рецепт',
        'recipe': recipe,
    }
    return render(request, 'good_eats/single_recipe.html', context)


def add_recipe(request):
    return HttpResponse('wow!')


def change_recipe(request, recipe_id):
    return HttpResponse(f'{recipe_id}')
