
from django.contrib.auth.models import AbstractUser
from django.db import models
# from social_media.models import Post, Discussion


class UserProfile(AbstractUser):
    my_location = models.CharField(max_length=60, blank=True)
    my_status = models.TextField(null=True, blank=True)
    subscribers = models.ManyToManyField(
        "self",
        symmetrical=False,
        blank=True,
        related_name="followed_users",
    )
    profile_pic = models.ImageField(blank=True, null=True, default="default.png")
    my_liked_posts = models.ManyToManyField(
        "social_media.Post", blank=True, related_name="users_liked"
    )
    my_liked_comments = models.ManyToManyField(
        "social_media.Discussion", blank=True, related_name="users_liked"
    )

    class Meta:
        ordering = ["username"]

    def number_of_followers(self):
        pass

    def number_of_following(self):
        pass
