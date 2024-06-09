from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('blog/', views.blog, name='Blog'),
    path('portfolio/', views.portfolio, name='Portfolio'),
    path('portfolio/<slug>', views.portfolio_details, name='PortfolioDetails'),
    path('blog/<slug>/', views.post_details, name='PostDetails'),
    path('contact/', views.contact, name='Contact'),
    path('contact/send_message/', views.send_message, name='send_message')
]
