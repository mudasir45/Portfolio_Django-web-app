from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import EmailMessage 
from django.template.loader import render_to_string
from django.conf import settings

from .models import *
from .forms import PostForm
from .filters import PostFilter

POSTS_PER_PAGE = 2
def postlist(request):
    posts = Post.objects.all()
    filterobj = PostFilter(request.GET, queryset = posts)
    posts = filterobj.qs
    
    page = request.GET.get('page', 1)
    PostPaginator = Paginator(posts, POSTS_PER_PAGE)
    
    try:
        posts = PostPaginator.page(page)
    except PageNotAnInteger:
        posts = PostPaginator.page(1)
    except EmptyPage:
        posts = PostPaginator.page(PostPaginator.num_pages)
    
    context = {
        'posts' : posts,
        'filterobj' : filterobj,
        'paginator' : PostPaginator,
        'IsPaginated' : True,
    }
    return render(request, 'post_list.html', context)

def single_post(request, slug):
    post_obj = Post.objects.get(slug = slug)
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
def edit_post(request, slug):
    post_obj = Post.objects.get(slug = slug)
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
def delete_post(request, slug):
    post_obj = Post.objects.get(slug = slug)
    
    if request.method == 'POST':
        post_obj.delete()
        return redirect(reverse('postlist'))
    
    context = {
        'item': post_obj
    } 
    return render(request, 'deletePost.html', context)


def sendMail(request):
    if request.method == 'POST':
        template = render_to_string('emailTemplate.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message']
        })
        
        email = EmailMessage(
            request.POST['subject'],
            template, 
            settings.EMAIL_HOST_USER,
            ['mudasiramin320@gmail.com']
        )
        email.fail_silently = False
        email.send()
    return render(request, 'emailSent.html')
    