import os
import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _

# from social_media.models import Post, Discussion


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


def user_profile_picture_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.username)}-{uuid.uuid4()}{extension}"

    return os.path.join(
        "uploads", "users", instance.username, "profile_picture", filename
    )


class UserProfile(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(blank=True, null=True, max_length=150)
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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ["username"]

    def number_of_followers(self):
        pass

    def number_of_following(self):
        pass
