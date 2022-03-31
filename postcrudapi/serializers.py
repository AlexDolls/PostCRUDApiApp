from rest_framework import serializers
from .models import Post, Comment



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk','title', 'link', 'creation_date', 'upvotes', 'author_name')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk', 'post', 'author_name', 'creation_date', 'content')

