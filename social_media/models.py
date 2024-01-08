from django.conf import settings
from django.db import models
from user.models import UserProfile


class Post(models.Model):
    image = models.ImageField(blank=False, null=False)
    location = models.TextField(null=True)
    description = models.TextField(null=True, max_length=144)
    tag_people = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="tags", blank=True
    )
    hash_tags = models.CharField(max_length=100, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(UserProfile, related_name="liked_posts", blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ["created_at"]


class Discussion(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="discussions")


class Message(models.Model):
    sender = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="received_messages"
    )
    body = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.sender.username} and {self.receiver.username}"

    class Meta:
        ordering = ["timestamp"]
