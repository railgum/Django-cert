from django.urls import path
from good_eats import views

# app_name = "good_eats"

urlpatterns = [
    path('', views.index, name='home'),
    path('recipe/<int:recipe_id>/', views.single_recipe, name='recipe'),
    path('add_recipe/', views.add_recipe, name='add'),
    path('change_recipe/<int:recipe_id>/', views.change_recipe, name='change'),
]
