from django.urls import path
from rest_framework import views

from user.views import CreateUserView, ManageUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateUserView.as_view(), name="token_obtain_pair"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"
