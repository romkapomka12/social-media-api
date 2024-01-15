from django.urls import path
from rest_framework import views

from user.views import (
    CreateUserView,
    ManageUserView,
    UpdatePasswordView,
    CreateTokenView,
)

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="token"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("me/password-change/", UpdatePasswordView.as_view(), name="password-change"),
]

app_name = "user"
