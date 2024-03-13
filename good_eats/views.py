from django.shortcuts import render, HttpResponse, Http404, get_object_or_404, redirect
from random import choice
from .forms import *


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


def all_recipe(request):
    recipes = Recipe.objects.all()

    context = {
        'title': 'Все рецепты',
        'recipes': recipes,
    }
    return render(request, 'good_eats/all_recipe.html', context)


def single_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {
        'title': 'Рецепт',
        'recipe': recipe,
    }
    return render(request, 'good_eats/single_recipe.html', context)


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    context = {
        'title': 'Добавить рецепт',
        'form': form,
    }
    return render(request, 'good_eats/add_recipe_form.html', context)


def change_recipe(request, recipe_id):
    old_recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=old_recipe)
        if form.is_valid():
            old_recipe = form.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=old_recipe)
    context = {
        'title': 'Изменить рецепт',
        'form': form,
    }
    return render(request, 'good_eats/add_recipe_form.html', context)
