# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post, Comment, Profile

# Create your views here.
def base(request):
    return render(request,'home.html')

def wall(request):
    posts = Post.objects.all()
    return render(request, 'user_wall.html', { "posts" : posts })

def profile(request,pk):
    # profile.user.pk
    # profile = Profile.objects.get(id = pk)
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(author = request.user.id)
    return render(request, 'profile.html', { "profile" : profile, "posts": posts })

def new_hike(request):
    user = request.user
    if request.method == 'POST':
        description = request.POST['description']
        distance_hiked = request.POST['distance_hiked']
        photo_url = request.POST['photo_url']

        post = Post.objects.create(
            author = user,
            description = description,
            distance_hiked = distance_hiked,
            photo_url = photo_url
        )

        post.save()

        return redirect('wall')
    else:
        return render(request, 'post.html', {'error': 'Something went wrong with your post'})
