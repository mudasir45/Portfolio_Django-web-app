from django.urls import path
from . import views

urlpatterns = [
    path('postlist/', views.postlist, name='postlist'),
    path('post/', views.post, name='post'),
]