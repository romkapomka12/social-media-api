from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from social_media.models import Post, Message


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()


class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related("user")


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
