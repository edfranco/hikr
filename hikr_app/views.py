# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
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

def new_hike(request):
    if request.method == 'POST':
        description = request.POST['description']
        distance = request.distance['distance']
        photo_url = request.photo_url['photo_url']

        post = Post.objects.create(
            description = description,
            distance = distance,
            photo_url = photo_url
        )

        post.save()

        return redirect('wall')
    else:
        return render(request, 'user_wall.html', {'error': 'Something went wrong with your post'})