from django.urls import path
from recipes.views import home, contatos, sobre

urlpatterns = [
    path('', home),
    path('contatos/', contatos),
    path('sobre/', sobre),
]