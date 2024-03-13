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
            'author': 'автор',
            'title': 'название',
            'image': 'изображение',
            'description': 'описание',
            'steps': 'шаги приготовления',
            'cooking_time': 'время приготовления',
            'date_pub': 'дата публикации',
            'ingridients': 'ингридиенты(если несколько - зажмите Ctrl)',
            'categories': 'категория',
        }
