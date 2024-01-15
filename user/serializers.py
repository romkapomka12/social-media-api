from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password", "is_staff")
        read_only_fields = ("id", "is_staff")
        extra_kwargs = {"password": {"write_only": True, "min_length": 6}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, set the password correctly and return it"""

        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class ManageUserSerializer(UserSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "full_name",
            "my_status",
            "my_location",
            "profile_pic",
            "is_staff",
        )
        read_only_fields = (
            "is_staff",
            "profile_pic",
        )


class UpdatePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_the_new_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ("old_password", "new_password", "confirm_the_new_password")

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_the_new_password"]:
            raise serializers.ValidationError(
                {"new_password": "Password fields didn't match."}
            )

        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )
        return value

    def update(self, instance, validated_data):
        """Update a user, set the password correctly and return it"""
        user = instance

        user.set_password(validated_data.get("new_password", None))
        user.save()

        return user




class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email")
    password = serializers.CharField(
        label="Password",
        style={"input_type": "password"},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                email=email,
                password=password
            )
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
            if not user.is_active:
                msg = _("User account is disabled.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        return {"user": user}
