from django.shortcuts import render
from django.http import HttpResponse

def index(requeste):
    return HttpResponse("Rango says hey there partner")

# Create your views here.
