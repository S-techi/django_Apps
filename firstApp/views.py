from django.shortcuts import render
from django.http import HttpResponse
'''
a view will take a response as  a parameter and return either a http response or render a template
'''
# Create your views here.
def produceSector(request):
    return HttpResponse("Produce by nature choice!")

def greeting(request):
    return HttpResponse("Welcome to my site")

def name(request):
    return render(request , 'firstApp/index.html')

