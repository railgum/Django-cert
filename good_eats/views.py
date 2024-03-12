from django.shortcuts import render, HttpResponse, Http404
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

