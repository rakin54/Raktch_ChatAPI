from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Post

# Register your models here.

class Post_Display(admin.ModelAdmin):
    list_display = ("id","title","content","author","created_at","updated_at")


admin.site.register(Post, Post_Display)
