from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from post.models import Post, Discussion


class UserProfile(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=60, blank=True)
    full_name = models.CharField(max_length=200, null=True)
    my_location = models.CharField(max_length=60, blank=True)
    my_status = models.TextField(null=True, blank=True)
    subscribers = models.ManyToManyField(
        "self", symmetrical=False, related_name="followed_users"
    )
    profile_pic = models.ImageField(blank=True, null=True, default="default.png")
    my_liked_posts = models.ManyToManyField(
        Post, blank=True, related_name="users_liked"
    )
    my_liked_comments = models.ManyToManyField(
        Discussion, blank=True, related_name="users_liked"
    )

    class Meta:
        ordering = ["username"]

    def number_of_followers(self):
        pass

    def number_of_following(self):
        pass
