from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract: True
    
class Category(models.Model):
    name  = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.name
    
    
class Post(TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT  = "draft", "Draft"
        PUBLISHED = "published", "Published"
        
    title = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="posts"
        
    )
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    
    image_preview = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True
    )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.name
    
    
class Comment(TimeStampedModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    
    body = models.TextField()
    
    class Meta:
        ordering = ['-createdAt']
        
    def __str__(self):
        return f'Comment by {self.author.username} on'
        
class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    
    
    class Meta:
        unique_together = ('user', 'post')
    
        
#assignment - ikenosuh@gmail.com, 
# read and wite on meta class properties, 2pages each with google docs
#read on views, api views and views set