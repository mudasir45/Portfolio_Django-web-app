from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page")

def posts(request):
    return HttpResponse("posts page ")

def post(request):
    return HttpResponse("single post page")

def profile(request):
    return HttpResponse("profile page")
