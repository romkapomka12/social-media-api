from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from social_media.models import Post, Message
from social_media.serializers import (
    MessageListSerializer,
    PostListSerializer,
    PostDetailSerializer,
    UserListSerializer,
    UserDetailSerializer,
)


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        return UserListSerializer

    def get_queryset(self):
        user = self.request.query_params.get("user")
        location = self.request.query_params.get("location")

        queryset = self.queryset

        if user:
            queryset = queryset.filter(
                Q(username__icontains=user) | Q(full_name__icontains=user)
            )

        if location:
            queryset = queryset.filter(location__icontains=location)

        return queryset

    def perform_subscribe_action(self, subscribe_to, request, action_type):
        if subscribe_to.is_subscribed:
            return Response(
                "Користувач вже підписаний", status=status.HTTP_400_BAD_REQUEST
            )
        else:
            serializer = self.get_serializer(
                data={"subscribe_to": subscribe_to.id},
                context={"request": request, "action": action_type},
            )
            serializer.is_valid(raise_exception=True)
            result = serializer.perform_action(subscribe_to, request)
            return Response(result["message"], status=status.HTTP_200_OK)


@action(
    methods=["GET"],
    detail=True,
    url_path="subscribe",
    permission_classes=[IsAuthenticated],
)
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
