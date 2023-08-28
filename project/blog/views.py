from django.shortcuts import render
from .models import *

def postlist(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'post_list.html', context)

def post(request):
    return render(request, 'post.html')