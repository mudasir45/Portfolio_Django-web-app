from django.forms import ModelForm
from django import forms

from .models import *

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'
    
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }
    
