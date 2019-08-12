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
    comments = Comment.objects.all()
    return render(request, 'user_wall.html', { "posts" : posts, "comments": comments })

def profile(request,pk):
    profile = Profile.objects.get(id=pk)
    posts = Post.objects.filter(author=profile.user)
    comments = Comment.objects.all()
    
    length = len(posts)
    total_distance = 0
    for post in posts:
        total_distance = total_distance + post.distance_hiked
    
    return render(request, 'profile.html', { 
        "profile" : profile, 
        "posts": posts,  
        "length": length,
        "comments": comments,
        "total_distance": total_distance
        })

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
    if request.method == "POST":
        description = request.POST['description']
        distance_hiked = request.POST['distance_hiked']
        photo_url = request.POST['photo_url']
        
        post.description = description
        post.distance_hiked = distance_hiked
        post.photo_url = photo_url
        
        post.save()
        return redirect('wall')
    else: 
        return render(request, 'post_edit.html', {"post" : post})

def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    if request.user.pk is not post.author.pk:
        return redirect('wall')
    post.delete()
    return redirect('wall')

def comment_post(request,pk):
    user = request.user
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        content = request.POST['content']
        
        comment = Comment.objects.create(
            content = content,
            author = user,
            post = post
        )

        
        comment.save()
        return redirect('wall')
    
    else:
        return render(request, 'user_wall.html')
