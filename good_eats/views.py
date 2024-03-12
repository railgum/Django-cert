from django.shortcuts import render, HttpResponse, Http404
from .models import *


def index(request):
    return HttpResponse("Страница приложения рецептов.")

