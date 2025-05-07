from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['post_id'])
        serializer.save(post=post)

# CommentCreateView: This view allows creating a comment for a specific post. 
# The perform_create method ensures that the post is correctly linked to the comment when it is created.
# We’ll use post_id to specify which post the comment belongs to.

class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)


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
