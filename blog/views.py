from django.shortcuts import render
from rest_framework.views import ListAPIView, CreateAPIView
from blog.models import Post
from blog.serializers import PostListSerializer, PostSerializer, PostDetailSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

# A view is simply a python class of functions that recieves a http request
# and returns a http response

# class PostListView(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostListSerializer
    
# class PostView(CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get_serial_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'list':
            return PostDetailSerializer
        else:
            return PostSerializer