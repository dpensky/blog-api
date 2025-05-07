from .models import Post, Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'post']
        read_only_fields = ['id', 'created_at', 'post']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


# The CommentSerializer is a standard ModelSerializer.
# The PostSerializer includes a nested CommentSerializer for the comments field. This way, when you retrieve a post, it will also include its related comments.