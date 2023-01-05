from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path('', views.home, name="recipes"),
    path('recipes/', views.home, name="recipes"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
