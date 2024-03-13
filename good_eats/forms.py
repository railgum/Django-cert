from django import forms
from .models import Recipe, Ingridient, Category


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'author',
            'title',
            'image',
            'description',
            'steps',
            'cooking_time',
            'date_pub',
            'ingridients',
            'categories',
        )
        labels = {
            'author': 'Автор',
            'title': 'Название',
            'image': 'Изображение',
            'description': 'Описание',
            'steps': 'Шаги приготовления',
            'cooking_time': 'Время приготовления',
            'date_pub': 'Дата публикации',
            'ingridients': 'Ингридиенты(если несколько - зажмите Ctrl)',
            'categories': 'Категория',
        }
