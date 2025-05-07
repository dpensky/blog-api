from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


# ModelSerializer auto-generates fields based on the model.
# fields = '__all__' includes all model fields (title, content, created_at).

