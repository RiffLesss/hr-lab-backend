from contrib.drf.serializers import ModelSerializer
from hrlab.user.models import User, ViewPermission


class ViewPermissionReadForProfileSerializer(ModelSerializer):
    class Meta:
        model = ViewPermission
        fields = read_only_fields = [
            "id",
            "value",
        ]


class SelfProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = read_only_fields = [
            "id",
            "login",
            "first_name",
            "last_name",
            "middle_name",
            "education",
            "work_experience",
            "project_experience",
            "cv_link",
            "email",
            "phone",
            "role",
            "user_view_permissions"
        ]

    user_view_permissions = ViewPermissionReadForProfileSerializer(many=True, read_only=True)
