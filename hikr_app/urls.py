from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name = 'base'),
    path('wall', views.wall, name = 'wall'),
    path('users/<int:pk>', views.profile, name= 'profile'),
    path('new_hike/', views.new_hike, name="new_hike"),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
<<<<<<< HEAD
    path('delete_post/<int:pk>', views.delete_post, name="delete_post"),
    path('comment_post/<int:pk>', views.comment_post, name="comment_post"),
    path('like/post/<int:post_pk>/user/<int:user_pk>', views.like, name="like")
]
=======
    path('delete_post/<int:pk>', views.delete_post, name="delete_post")
]
>>>>>>> 7b075d0a328331c2370441d6a470751a4613140d
