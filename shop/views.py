from django.shortcuts import render
from django.http import HttpResponse

def shop(request):
    return HttpResponse("Shop app")
