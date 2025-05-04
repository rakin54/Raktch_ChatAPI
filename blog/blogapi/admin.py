from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.utils.html import format_html
from .models import Post

# Register your models here.

class Post_Display(admin.ModelAdmin):
    list_display = ("id","title","content","author","image_tag","created_at","updated_at")

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return "No Image"

    image_tag.short_description = 'Image Preview'


admin.site.register(Post, Post_Display)
