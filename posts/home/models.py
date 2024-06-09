from django.db import models

class PostItem(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.TextField(max_length=700)
    text = models.TextField(max_length=20000)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=50, default='default-slug')
    banner = models.ImageField(default='fallback.jpg', blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class PortfolioItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=700)
    github = models.CharField(max_length=50, default='https://www.github.com/alexkuznecov16')
    date = models.DateField(auto_now_add=False)
    slug = models.CharField(max_length=50, default='default-slug')
    banner = models.ImageField(default='fallback.jpg', blank=True)
    
    def __str__(self) -> str:
        return self.title