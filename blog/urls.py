from django.urls import path
from . import views

urlpatterns = [
    path('postlist/', views.postlist, name='postlist'),
    path('post/<str:slug>', views.single_post, name='post'),
    
    # post crud urls 
    path('add_post', views.add_post, name='add_post'),
    path('edit_post/<str:slug>', views.edit_post, name='edit_post'),
    path('delete_post/<str:slug>', views.delete_post, name='delete_post'),
    
    path('sendMail/', views.sendMail, name='sendMail'),
    
]