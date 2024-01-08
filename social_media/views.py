from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from social_media.models import Post, Message
from social_media.serializers import (
    MessageListSerializer,
    PostListSerializer,
    UserListSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        return UserListSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related("user")

    def get_serializer_class(self):
        return PostListSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()

    def get_serializer_class(self):
        return MessageListSerializer
