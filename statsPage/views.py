from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def statsPageView(request) :
    return HttpResponse('This is the stats Page')