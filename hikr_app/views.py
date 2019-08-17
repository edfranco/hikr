# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post, Comment, Profile, Like

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('wall')
    else:
        return render(request,'home.html')

def wall(request):
    posts = Post.objects.all().order_by('-date_posted')
    comments = Comment.objects.all()
    return render(request, 'user_wall.html', { 
        "posts" : posts, 
        "comments": comments,
        })

def profile(request,pk):
    profile = Profile.objects.get(id=pk)
    posts = Post.objects.filter(author=profile.user).order_by('-date_posted')
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
        
        })

def new_hike(request):
    user = request.user
    if request.method == 'POST':
        description = request.POST['description']
        location = request.POST['location']
        distance_hiked = request.POST['distance_hiked']
        photo_url = request.POST['photo_url']

        post = Post.objects.create(
            author = user,
            location = location,
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
        location = request.POST['location']
        distance_hiked = request.POST['distance_hiked']
        photo_url = request.POST['photo_url']
        

        post.description = description
        post.location = location
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
    profile = Profile.objects.get(id=request.user.pk)
    if request.method == "POST":
        content = request.POST['content']
        comment = Comment.objects.create(
            content = content,
            author = user,
            post = post,
            profile=profile
        )
        comment.save()
        return redirect('wall')
    
    else:
        return render(request, 'user_wall.html')
def like(request,pk):
    liker = request.user
    post = Post.objects.get(id=pk)
    
    if request.method == "POST":
        like = Like.objects.create(
            liker = liker,
            post = post
        )
        # post.likes
        like.save()
        return redirect('wall')
    else:
        return render(request, 'user_wall.html')

def api(request):
    users = User.objects.all().values('pk','first_name','last_name')
    posts = Post.objects.all().values('pk','author','description')
    likes = Like.objects.all().values('pk', 'liker', 'post')
    users_list=list(users)
    posts_list=list(posts)
    likes_list=list(likes)
    data={
        "users":users_list,
        "posts":posts_list,
        "likes":likes_list
    }
    return JsonResponse(data,safe=False)

def find_location(request,pk):
    post = Post.objects.get(id=pk);
    
    return render(request, 'location_map.html', { "post" : post })

def about(request):
    scott = User.objects.get(pk=2)
    scott_profile = Profile.objects.get(pk=2)
    zafar = User.objects.get(pk=2)
    zafar_profile = Profile.objects.get(pk=2)
    eduardo = User.objects.get(pk=1)
    eduardo_profile = Profile.objects.get(pk=1)

    return render(request, 'about.html', { 
        "scott":scott,
        "scott_profile":scott_profile,
        "zafar":zafar,
        "zafar_profile":zafar_profile,
        "eduardo":eduardo,
        "eduardo_profile":eduardo_profile,
          })

