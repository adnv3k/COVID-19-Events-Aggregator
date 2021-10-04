from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse('Location configuration index.')

# Create your views here.
