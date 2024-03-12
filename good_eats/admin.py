from django.contrib import admin
from .models import Recipe, Category, Ingridient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_pub', ]
    search_fields = ['description']
    fieldsets = [
        (
            None, {
                'fields': ['title', 'author', 'image']
            }
        ),
        (
            'Дополнительно:', {
                'fields': [
                    'description',
                    'steps',
                    'cooking_time',
                    'date_pub',
                    'ingridients',
                    'categories', ]
            }
        )
    ]


@admin.register(Ingridient)
class IngridientAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    fieldsets = [
        (
            None, {
                'fields': ['name']
            }
        )
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    fieldsets = [
        (
            None, {
                'fields': ['name']
            }
        )
    ]
