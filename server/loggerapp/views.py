from django.shortcuts import render, HttpResponse
from . import views

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

    