from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post

# from .models import Artist, Song

class SignupForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'password')

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['description', 'distance_hiked', 'photo_url']
