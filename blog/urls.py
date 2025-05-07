from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentCreateView, CommentListView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comments/create/', CommentCreateView.as_view(), name='comment-create'),
]

#  POST /posts/<post_id>/comments/: Create a comment for the specified post.