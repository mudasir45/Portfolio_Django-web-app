from django.shortcuts import render, redirect
from .models import *
from .forms import *

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
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('postlist/')
    
    context = {
        'form': form
    } 
    return render(request, 'add_post.html', context)
