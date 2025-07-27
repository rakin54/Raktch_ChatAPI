from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author','image', 'created_at', 'updated_at']
        read_only_fields = ['author','created_at', 'updated_at']







