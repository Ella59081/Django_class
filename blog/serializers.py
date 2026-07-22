from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at']
        
class PostListSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author_username', read_only=True)
    category_name = serializers.CharField(source='category_name', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', ]
        
    def validate_title(self, value):
        if len(value) > 100:
            raise serializers.ValidationError(
                "Title is too long"
            )
        return value
        
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        models = Post
        fields = ['id', 'title', 'slug']
        

class PostSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'likes', 'description', 'category', 'author', 'created_at']
        
    def validate_title(self, value):
        if len(value) > 100:
            raise serializers.ValidationError(
                "Title is too long"
            )
        return value
        
    