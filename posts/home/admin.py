from django.contrib import admin
from .models import PostItem, PortfolioItem

# Register your models here.
admin.site.register(PostItem)
admin.site.register(PortfolioItem)