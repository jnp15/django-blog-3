from django.contrib.auth.models import User
from rest_framework import serializers
from blogging.models import Post, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            "url",
            "title",
            "text",
            "created_date",
            "modified_date",
            "published_date",
            "author",
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["url", "name", "description", "posts"]
