
from django.contrib.auth.models import UserAdmin
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    class Role(models.TextChoices):
        READER = 'reader', 'Reader'
        AUTHOR = 'author', 'Author'
    
    
    role = models.CharField(
        max_length= 10,
        choices=Role.choices,
        default=Role.READER
    )
    
    bio = models.TextField(blank= True)
    
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True
    )
    
    
    def __str__(self):
        return self.username