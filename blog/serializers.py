from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at']
        
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        models = Post
        fields = ['id', 'title', 'slug']  