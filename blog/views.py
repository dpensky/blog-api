from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# What these views do:
# ListCreateAPIView:
# GET → list all posts
# POST → create a new post
# RetrieveUpdateDestroyAPIView:
# GET → retrieve a single post
# PUT / PATCH → update
# DELETE → delete
