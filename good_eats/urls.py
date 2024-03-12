from django.urls import path
from . import views

app_name = "good_eats"

urlpatterns = [
    path('', views.index, name='home'),
]
