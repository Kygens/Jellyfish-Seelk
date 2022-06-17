from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request):
    return HttpResponse("Hello world! You are at the user index.")
# Create your views here.


