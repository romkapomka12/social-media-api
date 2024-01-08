from django.contrib.auth import get_user_model
from rest_framework import serializers

from social_media.models import Post, Message


class PostListSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ("id", "created_at", "description", "image", "author")
        read_only_fields = ["author"]


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "full_name",
            "profile_pic"
        )


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "sender", "receiver", "body", "timestamp")
        read_only_fields = ["body"]

