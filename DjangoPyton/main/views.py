from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h4>Hello World!</h4>")


def about(request):
    return HttpResponse("<h4>Про нас</h4>")