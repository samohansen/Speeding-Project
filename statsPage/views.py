from django.shortcuts import render
from django.http import HttpResponse

def statsPageView(request):
    return render(request, 'statsPage/showData.html')

def enterDataPageView(request):
    return render(request, 'statsPage/enterData.html')