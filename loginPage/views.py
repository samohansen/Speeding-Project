from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'loginPage/index.html')

def aboutPageView(request):
    return render(request, 'loginPage/about.html')

def loginPageView(request):
    return render(request, 'loginPage/login.html')

# def loginPageView(request) :
#     return HttpResponse('This is the Login Page')

# def aboutPageView(request):
#     return HttpResponse('Hi its the about')

# def statsPageView(request) :
#     return HttpResponse('This is the stats Page')