# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
<<<<<<< HEAD
from .models import Post, Comment, Profile, Like
=======
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Profile
from .forms import PostForm
>>>>>>> 7b075d0a328331c2370441d6a470751a4613140d

# Create your views here.
def home(request):
    return render(request,'base.html')

def wall(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    likes = Like.objects.all()
    return render(request, 'user_wall.html', { 
        "posts" : posts, 
        "comments": comments,
        "likes" : likes 
        })

<<<<<<< HEAD
def profile(request,pk):
    profile = Profile.objects.get(id=pk)
    posts = Post.objects.filter(author=profile.user)
    comments = Comment.objects.all()
    likes = Like.objects.all()
    
    length = len(posts)
    total_distance = 0
    for post in posts:
        total_distance = total_distance + post.distance_hiked
    
    return render(request, 'profile.html', { 
        "profile" : profile, 
        "posts": posts,  
        "length": length,
        "comments": comments,
        "total_distance": total_distance,
        "likes" : likes
        })
=======
def profile(request, pk):
    # profile.user.pk
    #profile = Profile.objects.get(id = pk)
    # profile = request.user.post_author
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(author = request.user.id)
    return render(request, 'profile.html', { "profile" : profile, "posts": posts })
>>>>>>> 7b075d0a328331c2370441d6a470751a4613140d

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


<<<<<<< HEAD
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
def like(request,pk):
    user = request.user
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        like = Like.objects.create(
            user = user,
            post = post
        )
        like.save()
        return redirect('wall')
    else:
        return render(request, 'user_wall.html')

=======
>>>>>>> 7b075d0a328331c2370441d6a470751a4613140d
