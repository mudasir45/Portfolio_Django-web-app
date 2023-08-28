from django.shortcuts import render

def postlist(request):
    return render(request, 'post_list.html')

def post(request):
    return render(request, 'post.html')