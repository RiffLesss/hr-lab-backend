from rest_framework import serializers

from contrib.drf.serializers import ModelSerializer
from hrlab.jobopen.models import JobOpen
from hrlab.laboratory.models import Laboratory
from hrlab.project.models import Project
from hrlab.user.models import User


class UserSerializerForProjectSerializer(ModelSerializer):
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


class LaboratorySerializerForProjectSerializer(ModelSerializer):
    class Meta:
        model = Laboratory
        fields = read_only_fields = [
            "id",
            "name",
            "link",
            "manager"
        ]

    manager = UserSerializerForProjectSerializer()


class JobOpenReadSerializer(ModelSerializer):
    class Meta:
        model = JobOpen
        fields = read_only_fields = [
            "id",
            "name",
            "requirements",
            "salary",
        ]


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = read_only_fields = [
            "id",
            "name",
            "budget",
            "manager",
            "project_deadline",
            "application_deadline",
            "laboratory",
            "jobs"
        ]

    manager = UserSerializerForProjectSerializer()

    laboratory = LaboratorySerializerForProjectSerializer()

    jobs = JobOpenReadSerializer(read_only=True, many=True)


class CreateProjectSerializer(ModelSerializer):
    class Meta:
        response_serializer_class = ProjectSerializer
        model = Project
        fields = read_only_fields = [
            "id",
            "name",
            "budget",
            "manager",
            "project_deadline",
            "application_deadline",
            "laboratory",
        ]

    name = serializers.CharField()

    budget = serializers.IntegerField()

    manager = serializers.PrimaryKeyRelatedField(write_only=True,
                                                 queryset=User.objects.filter(is_deleted=False),
                                                 required=True)

    project_deadline = serializers.DateField()

    application_deadline = serializers.DateField()

    laboratory = serializers.PrimaryKeyRelatedField(write_only=True,
                                                    queryset=Laboratory.objects.filter(is_deleted=False),
                                                    required=True)


class UpdateProjectSerializer(ModelSerializer):
    class Meta:
        response_serializer_class = ProjectSerializer
        model = Project
        fields = read_only_fields = [
            "id",
            "name",
            "budget",
            "manager",
            "project_deadline",
            "application_deadline",
            "laboratory",
            "is_deleted",
            "is_archived"
        ]

    name = serializers.CharField(required=False)

    budget = serializers.IntegerField(required=False)

    manager = serializers.PrimaryKeyRelatedField(write_only=True,
                                                 queryset=User.objects.filter(is_deleted=False),
                                                 required=False)

    project_deadline = serializers.DateField(required=False)

    application_deadline = serializers.DateField(required=False)

    laboratory = serializers.PrimaryKeyRelatedField(write_only=True,
                                                    queryset=Laboratory.objects.filter(is_deleted=False),
                                                    required=False)

    is_deleted = serializers.BooleanField(write_only=True, required=False)

    is_archived = serializers.BooleanField(write_only=True, required=False)