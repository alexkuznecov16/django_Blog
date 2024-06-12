from django.shortcuts import render, redirect
from .models import PostItem, PortfolioItem
# from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
  latest_portfolio = PortfolioItem.objects.order_by('-date')[:3]
  latest_posts = PostItem.objects.order_by('-date')[:4]
  context = {
      'portfolio': latest_portfolio,
      'latest_posts': latest_posts,
  }
  return render(request, 'base.html', context)


def blog(request):
  items = PostItem.objects.all()
  return render(request, 'blog.html', {"posts": items})


def portfolio(request):
  items = PortfolioItem.objects.all().order_by('-date')
  return render(request, 'portfolio.html', {"portfolio": items})


def portfolio_details(request, slug):
    item = PortfolioItem.objects.get(slug=slug)
    return render(request, 'portfolio_details.html', {'portfolio': item})


def post_details(request, slug):
    post = PostItem.objects.get(slug=slug)
    return render(request, 'post_details.html', {'post': post})
  
  
def contact(request):
  return render(request, 'contact.html')


import yagmail
from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            yag = yagmail.SMTP('alexander.kuznecov16@gmail.com', 'flwv gccy igmn qhgt')
            yag.send(to='alexander.kuznecov16@gmail.com', subject=subject, contents=f'From: {name}\nEmail: {email}\n\n{message}')
            return HttpResponse('Message sent successfully.')
        except Exception as e:
            return HttpResponse(f'Error sending message: {e}')

    return render(request, 'contact.html')
    
    
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)