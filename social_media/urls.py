from django.db import router
from django.urls import path, include
from rest_framework import routers

from social_media.views import UserViewSet, MessageViewSet, PostViewSet

router = routers.DefaultRouter()

router.register("users", UserViewSet)
router.register("posts", PostViewSet)
router.register("message", MessageViewSet)


urlpatterns = [
    path("", include(router.urls))]

app_name = "social_media"
