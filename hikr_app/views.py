# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post, Comment, Profile

# Create your views here.
def home(request):
    return render(request,'base.html')

def wall(request):
    posts = Post.objects.all()
    return render(request, 'user_wall.html', { "posts" : posts })

def profile(request,pk):
    # profile.user.pk
    profile = Profile.objects.get(id = pk)
    posts = Post.objects.filter(author = profile.user)
    return render(request, 'profile.html', { "profile" : profile, "posts": posts })