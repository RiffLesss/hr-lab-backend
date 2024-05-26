from rest_framework import serializers

from contrib.drf.serializers import ModelSerializer
from hrlab.laboratory.models import Laboratory
from hrlab.project.models import Project
from hrlab.user.models import User


class UserSerializerForLaboratorySerializer(ModelSerializer):
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
            "role"
        ]


class LaboratorySerializer(ModelSerializer):
    class Meta:
        model = Laboratory
        fields = read_only_fields = [
            "id",
            "name",
            "link",
            "manager"
        ]

    manager = UserSerializerForLaboratorySerializer()


class CreateLaboratorySerializer(ModelSerializer):
    class Meta:
        response_serializer_class = LaboratorySerializer
        model = Laboratory
        fields = read_only_fields = [
            "id",
            "name",
            "link",
            "manager"
        ]

    name = serializers.CharField()

    link = serializers.CharField()

    manager = serializers.PrimaryKeyRelatedField(write_only=True,
                                                 queryset=User.objects.filter(is_deleted=False),
                                                 required=True)


class UpdateLaboratorySerializer(ModelSerializer):
    class Meta:
        response_serializer_class = LaboratorySerializer
        model = Laboratory
        fields = read_only_fields = [
            "id",
            "name",
            "link",
            "manager",
            "is_deleted",
            "is_archived"
        ]

    name = serializers.CharField(required=False)

    link = serializers.CharField(required=False)

    manager = serializers.PrimaryKeyRelatedField(write_only=True,
                                                 queryset=User.objects.filter(is_deleted=False),
                                                 required=False)

    is_deleted = serializers.BooleanField(write_only=True, required=False)

    is_archived = serializers.BooleanField(write_only=True, required=False)