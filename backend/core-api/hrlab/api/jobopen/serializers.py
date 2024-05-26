from rest_framework import serializers

from contrib.drf.serializers import ModelSerializer
from hrlab.jobopen.models import JobOpen
from hrlab.laboratory.models import Laboratory
from hrlab.project.models import Project
from hrlab.user.models import User


class UserSerializerForJobOpenSerializer(ModelSerializer):
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


class LaboratorySerializerForJobOpenSerializer(ModelSerializer):
    class Meta:
        model = Laboratory
        fields = read_only_fields = [
            "id",
            "name",
            "link",
            "manager"
        ]

    manager = UserSerializerForJobOpenSerializer()


class ProjectSerializerForJobOpenSerializer(ModelSerializer):
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
        ]

    manager = UserSerializerForJobOpenSerializer()

    laboratory = LaboratorySerializerForJobOpenSerializer()


class JobOpenSerializer(ModelSerializer):
    class Meta:
        model = JobOpen
        fields = read_only_fields = [
            "id",
            "name",
            "requirements",
            "salary",
            "project"
        ]

    project = ProjectSerializerForJobOpenSerializer()


class CreateJobOpenSerializer(ModelSerializer):
    class Meta:
        response_serializer_class = JobOpenSerializer
        model = JobOpen
        fields = read_only_fields = [
            "id",
            "name",
            "requirements",
            "salary",
            "project"
        ]

    name = serializers.CharField()

    requirements = serializers.CharField()

    salary = serializers.IntegerField()

    project = serializers.PrimaryKeyRelatedField(write_only=True,
                                                 queryset=Project.objects.filter(is_deleted=False),
                                                 required=True)


class UpdateJobOpenSerializer(ModelSerializer):
    class Meta:
        response_serializer_class = JobOpenSerializer
        model = JobOpen
        fields = read_only_fields = [
            "id",
            "name",
            "requirements",
            "salary",
            "project",
            "is_deleted",
            "is_archived"
        ]

    name = serializers.CharField(required=False)

    requirements = serializers.CharField(required=False)

    salary = serializers.IntegerField(required=False)

    project = serializers.PrimaryKeyRelatedField(write_only=True,
                                                 queryset=Project.objects.filter(is_deleted=False),
                                                 required=False)

    is_deleted = serializers.BooleanField(write_only=True, required=False)

    is_archived = serializers.BooleanField(write_only=True, required=False)