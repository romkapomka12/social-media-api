from datetime import datetime, date

from django.contrib.auth import get_user_model
from rest_framework import serializers

from social_media.models import Post, Message


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "image",
            "description",
            "likes",
        )
        read_only_fields = ["author"]


class PostDetailSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    hash_tags = serializers.CharField(max_length=50, allow_blank=True, default="")

    class Meta:
        model = Post
        fields = (
            "id",
            "image",
            "location",
            "description",
            "tag_people",
            "hash_tags",
            "likes",
            "author",
            "days_since_created",
        )
        read_only_fields = ["author"]


    def get_days_since_created(self, obj):
        days_passed = (date.today() - obj.created_at.date()).days
        if days_passed == 0:
            return f"today"
        return f"{days_passed} days ago"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        hash_tags = representation.get("hash_tags", "")
        if hash_tags:
            tags_list = hash_tags.split(",")
            formatted_tags = ["#" + tag.strip() for tag in tags_list]
            representation["hash_tags"] = ", ".join(formatted_tags)

        return representation


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "full_name", "profile_pic",  "subscribers_count")


class UserPostSerializer(UserListSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "profile_pic", "full_name", "username")


class UserDetailSerializer(serializers.ModelSerializer):
    subscribes_to = UserListSerializer(many=True)
    subscribers = UserListSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "profile_pic",
            "username",
            "full_name",
            "description",
            "location",
            "subscribers_count",
            "subscribers",
            "subscribers_to",
        )

class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "sender", "receiver", "body", "timestamp")
        # read_only_fields = ["body"]
