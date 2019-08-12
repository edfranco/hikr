from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name = 'base'),
    path('wall', views.wall, name = 'wall'),
    path('users/<int:pk>', views.profile, name= 'profile'),
    path('new_hike/', views.new_hike, name="new_hike"),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>', views.delete_post, name="delete_post"),
    path('comment_post/<int:pk>', views.comment_post, name="comment_post"),
    path('like/post/<int:post_pk>/user/<int:user_pk>', views.like, name="like")
]