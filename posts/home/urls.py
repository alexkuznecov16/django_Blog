from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('posts/', views.posts, name='Posts'),
    path('posts/<slug>/', views.post_details, name='PostDetails'),
]
