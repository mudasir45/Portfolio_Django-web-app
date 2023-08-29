from django.shortcuts import render
from .models import *

def postlist(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'post_list.html', context)

def single_post(request, id):
    post_obj = Post.objects.get(id = id)
    context = {
        'post_obj':post_obj,
    }
    return render(request, 'post.html', context)


# Post Crud starts from here 
def add_post(request):
    
    return render(request, 'add_post.html')
