import logging

from django.contrib import auth
from django.contrib.auth import user_logged_in
from django.contrib.auth.hashers import make_password
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from contrib.drf.serializers import Serializer, ModelSerializer
from hrlab import settings
from hrlab.user.models import User
from hrlab.user.utils import get_tokens_for_user

logger = logging.getLogger(__name__)


class AuthTokenSerializer(serializers.Serializer):
    refreshToken = serializers.CharField(read_only=True)
    accessToken = serializers.CharField(read_only=True)

    refreshTokenExpiresIn = serializers.IntegerField(read_only=True)
    accessTokenExpiresIn = serializers.IntegerField(read_only=True)

    def to_representation(self, user: User):
        return get_tokens_for_user(user)


class SignInSerializer(Serializer):
    class Meta:
        response_serializer_class = AuthTokenSerializer

    default_error_messages = {
        "invalid_credentials": "Please enter a correct email and password.",
    }

    login = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, trim_whitespace=False, style={"input_type": "password"})

    def validate(self, data: dict):
        request = self.context["request"]
        request.data['login'] = request.data['login'].lower()
        user = auth.authenticate(request=request, **data)
        if not user:
            self.fail("invalid_credentials")
        self.context["user"] = user
        return data

    def create(self, validated_data):
        user = self.context["user"]
        user_logged_in.send(user.__class__,
                            request=self.context["request"],
                            user=user)
        return user


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = read_only_fields = [
            "id",
            "login",
            "password",
            "first_name",
            "last_name",
            "middle_name",
            "education",
            "work_experience",
            "project_experience",
            "cv_link",
            "email",
            "phone"
        ]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user

    login = serializers.CharField(write_only=True)

    password = serializers.CharField(write_only=True)

    first_name = serializers.CharField(write_only=True)

    last_name = serializers.CharField(write_only=True)

    middle_name = serializers.CharField(write_only=True)

    education = serializers.CharField(write_only=True)

    work_experience = serializers.CharField(write_only=True)

    project_experience = serializers.CharField(write_only=True)

    cv_link = serializers.CharField(write_only=True)

    email = serializers.EmailField(write_only=True)

    phone = PhoneNumberField(region="RU")
