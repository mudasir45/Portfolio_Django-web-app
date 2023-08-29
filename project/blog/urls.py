from django.urls import path
from . import views

urlpatterns = [
    path('postlist/', views.postlist, name='postlist'),
    path('post/<int:id>', views.single_post, name='post'),
    
    # post crud urls 
    path('add_post', views.add_post, name='add_post'),
    path('edit_post/<int:id>', views.edit_post, name='edit_post'),
    
]