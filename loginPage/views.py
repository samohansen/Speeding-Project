from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def loginPageView(request) :
    return HttpResponse('This is the Login Page')

def aboutPageView(request):
    return HttpResponse('Hi its the about')

# def statsPageView(request) :
#     return HttpResponse('This is the stats Page')