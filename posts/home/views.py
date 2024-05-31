from django.shortcuts import render
from .models import PostItem

# Create your views here.
def home(request):
  latest_posts = PostItem.objects.order_by('-date')[:4]
  return render(request, 'home.html', {'latest_posts': latest_posts})


def posts(request):
  items = PostItem.objects.all()
  return render(request, 'posts.html', {"posts": items})

def post_details(request, slug):
    post = PostItem.objects.get(slug=slug)
    return render(request, 'post_details.html', {'post': post})