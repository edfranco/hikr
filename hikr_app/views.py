# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def home(request):
    return render(request,'home.html')

def wall(request):
    posts = Post.objects.all()
    return render(request, 'user_wall.html', { "posts" : posts })
