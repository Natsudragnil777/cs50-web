from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request , "hello/index.html")

def saif(request):
    return HttpResponse("hello, saif")

def david(request):
    return HttpResponse("hello, david")

def great(request , name):
    return render(request , "hello/great.html" , {"name":name.capitalize()})
