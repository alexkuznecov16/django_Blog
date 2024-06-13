from django.shortcuts import render
from .models import PostItem, PortfolioItem
from django.core.mail import send_mail
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


@csrf_exempt
def send_message(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Name: {name}\nEmail: {email}\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                'alexander.kuznecov16@gmail.com',
                ['alexdevscript@gmail.com'],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Error sending email: {e}")
            return HttpResponse(f'Error sending email. {e}')

        html_response = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Message Sent</title>
            <script>
                setTimeout(function() {
                    window.location.href = "/";
                }, 3000);
            </script>
        </head>
        <body>
            <p>Message sent successfully. Redirecting...</p>
        </body>
        </html>
        """
        return HttpResponse(html_response)
    else:
        return HttpResponse('Invalid request.')

    
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)