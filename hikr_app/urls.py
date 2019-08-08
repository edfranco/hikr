from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('wall', views.wall, name = 'wall'),
    path('users/<int:pk>', views.profile, name= 'profile'),
    path('new_hike', views.new_hike, name="new_hike")
]