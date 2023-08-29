from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
login_required(login_url='/')
def add_post(request):
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('postlist')
    
    context = {
        'form': form
    } 
    return render(request, 'add_post.html', context)


login_required(login_url='/')
def edit_post(request, id):
    post_obj = Post.objects.get(id = id)
    form = PostForm(instance=post_obj)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post_obj)
        if form.is_valid():
            form.save()
        return redirect(reverse('postlist'))
    
    context = {
        'form': form
    } 
    return render(request, 'add_post.html', context)


login_required(login_url='/')
def delete_post(request, id):
    post_obj = Post.objects.get(id = id)
    
    if request.method == 'POST':
        post_obj.delete()
        return redirect(reverse('postlist'))
    
    context = {
        'item': post_obj
    } 
    return render(request, 'deletePost.html', context)
