from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def about(request):
    return HttpResponse('about us')


def index(request):
    return HttpResponse('index page')