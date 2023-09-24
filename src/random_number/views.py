from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.

def get_random(request):
    return HttpResponse (f"<h3>Result:</h3> {str(randint(0, 100_000))}")
