from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from social_media.models import Post, Message
from social_media.serializers import (
    MessageListSerializer,
    PostListSerializer,
    PostDetailSerializer,
    UserListSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        return UserListSerializer


class PostViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == "list" or self.action == "create":
            return PostListSerializer

        if self.action == "retrieve":
            return PostDetailSerializer

        return PostListSerializer


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()

    def get_serializer_class(self):
        return MessageListSerializer
