from datetime import datetime

from rest_framework import serializers

from contrib.drf.serializers import ModelSerializer
from hrlab.application.models import Application
from hrlab.jobopen.models import JobOpen
from hrlab.laboratory.models import Laboratory
from hrlab.project.models import Project
from hrlab.user.models import User


class UserSerializerForApplicationSerializer(ModelSerializer):
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


class LaboratorySerializerForApplicationSerializer(ModelSerializer):
    class Meta:
        model = Laboratory
        fields = read_only_fields = [
            "id",
            "name",
            "link",
            "manager"
        ]

    manager = UserSerializerForApplicationSerializer()


class ProjectSerializerForApplicationSerializer(ModelSerializer):
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

    manager = UserSerializerForApplicationSerializer()

    laboratory = LaboratorySerializerForApplicationSerializer()


class JobOpenSerializerForApplicationSerializer(ModelSerializer):
    class Meta:
        model = JobOpen
        fields = read_only_fields = [
            "id",
            "name",
            "requirements",
            "salary",
            "project"
        ]

    project = ProjectSerializerForApplicationSerializer()


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = read_only_fields = [
            "id",
            "user",
            "status",
            "message",
            "job_open"
        ]

    job_open = JobOpenSerializerForApplicationSerializer()


class CreateApplicationSerializer(ModelSerializer):
    class Meta:
        response_serializer_class = ApplicationSerializer
        model = Application
        fields = read_only_fields = [
            "id",
            "user",
            "message",
            "job_open"
        ]

    def validate(self, attrs):
        application_deadline = attrs['job_open'].project.application_deadline
        if application_deadline >= datetime.now().date():
            return attrs
        else:
            raise serializers.ValidationError("Срок сбора заявок для данного проекта закончился.")

    serializers.HiddenField(default=serializers.CurrentUserDefault())

    message = serializers.CharField()

    job_open = serializers.PrimaryKeyRelatedField(write_only=True,
                                                 queryset=JobOpen.objects.filter(is_deleted=False),
                                                 required=True)


class UpdateApplicationSerializer(ModelSerializer):
    class Meta:
        response_serializer_class = ApplicationSerializer
        model = Application
        fields = read_only_fields = [
            "id",
            "message",
            "job_open",
            "is_deleted",
            "is_archived"
        ]

    message = serializers.CharField(required=False)

    job_open = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  queryset=JobOpen.objects.filter(is_deleted=False),
                                                  required=False)

    is_deleted = serializers.BooleanField(write_only=True, required=False)

    is_archived = serializers.BooleanField(write_only=True, required=False)


class RejectApplicationSerializer(serializers.Serializer):

    def update(self, instance: Application, validated_data):
        instance.status = Application.Status.REJECTED
        instance.save()
        return instance

    def to_representation(self, instance):
        return Application(self.context).to_representation(instance)


class ApproveApplicationSerializer(serializers.Serializer):

    def update(self, instance: Application, validated_data):
        instance.status = Application.Status.APPROVED
        instance.save()
        return instance

    def to_representation(self, instance):
        return Application(self.context).to_representation(instance)
