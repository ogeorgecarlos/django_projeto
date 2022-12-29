from django.urls import path
from recipes.views import about, index


urlpatterns = [
    path('sobre/', about),
    path('', index),
]