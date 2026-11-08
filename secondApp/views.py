from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def name(request):
    return HttpResponse("My name is Hannah"),

def nav(request):
     return render(request , 'secondApp/index.html')


