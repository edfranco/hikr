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
    profile = Profile.objects.get(id=pk)
    posts = Post.objects.filter(author=profile.user)
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

def edit_post(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == "PUT":
        post.update(
            description = description,
            distance_hiked = distance_hiked,
            photo_url = photo_url
        )
        post.save()
        return redirect('wall')
    else: 
        return render(request, 'post_edit.html', {'error' : 'Something went wrong with your edit', "post" : post})

def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    if request.user.pk is not post.author.pk:
        return redirect('wall')
    post.delete()
    return redirect('wall')
