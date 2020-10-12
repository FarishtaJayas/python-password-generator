from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('No Bye')

def games(request):
    return HttpResponse('<h1>Video Games Are The Best</h1>')

def ghash(request):
    return HttpResponse('<h2>Best Clothing Line In BD</h2>')