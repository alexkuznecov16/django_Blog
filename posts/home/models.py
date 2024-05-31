from django.db import models

class PostItem(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=20000)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=50, default='default-slug')
    banner = models.ImageField(default='fallback.jpg', blank=True)
    
    def __str__(self) -> str:
        return self.title