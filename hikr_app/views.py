# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Profile
from .forms import PostForm

# Create your views here.
def home(request):
    return render(request,'base.html')

def wall(request):
    posts = Post.objects.all()
    return render(request, 'user_wall.html', { "posts" : posts })

def profile(request, pk):
    # profile.user.pk
    #profile = Profile.objects.get(id = pk)
    # profile = request.user.post_author
    profile = Profile.objects.get(user = request.user)
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


def edit_hike(request, pk):
    one_post = Post.pbjects.get(pk=post_id)
    if request.method == 'POST':
        description = request.POST['description']
        disctance_hiked = request.POST['distance_hiked']
        photo_url = request.POST['photo_url']

        one_post = Post.objects.update(
            description = description,
            distmace_hiked = distance_hiked,
            photo_url = photo_url 
        )
        one_post.save()
        return redirect('wall')
    else:
        return render(request, 'post.html', {'error': 'Something went wrong with your post'})
    # form = PostForm(request.POST, instance=one_post)
    # if form.is_valid():
    #     form.save()
    # p_list = Post.objects.get(id=2) #all().filter(description__startswith='Test')
    # for thing in p_list:
        # print (thing)
        # description = request.GET['Description']
        # distance_hiked = request.GET['Distance_hiked']
        # photo_url = req
    # return render(request, 'profile.html', {'form': form , 'error': 'Something went wrong with your post'})
# def hike_delete(request, pk):
#     user = request.user.post_author
#     Post.objects.get(author = request.user.id).delete()
#     return render('profile')


# def like_post(request):
#     post_id = request.GET.get('post_id', None)

#     likes = 0
#     if (post_id):
#         post = Post.objects.get(id=int(post_id))
#         if cat is not None:
#             likes = post.likes + 1
#             post.likes = likes
#             post.save()
#     return HttpResponse(likes)
