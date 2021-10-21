from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world!")


def daniel(request):
    return HttpResponse("Hello, Daniel")


def greet(request, name):
    return HttpResponse(f"Hello, {name}!")
