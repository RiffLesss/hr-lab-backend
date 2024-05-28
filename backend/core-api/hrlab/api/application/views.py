from django.http import Http404
from drf_spectacular.utils import extend_schema
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter

from contrib.drf.viewsets import BaseViewSet
from hrlab.api.application.serializers import ApplicationSerializer, CreateApplicationSerializer, \
    UpdateApplicationSerializer, ApproveApplicationSerializer, RejectApplicationSerializer
from hrlab.api.jobopen.serializers import JobOpenSerializer, CreateJobOpenSerializer, UpdateJobOpenSerializer
from hrlab.application.models import Application
from hrlab.jobopen.models import JobOpen
from hrlab.laboratory.models import Laboratory


class ApplicationFilterSet(filters.FilterSet):
    class Meta:
        model = Application
        fields = {
            "user": ['exact'],
            "job_open": ['exact'],
            "is_deleted": ['exact'],
            "is_archived": ['exact'],
        }


@extend_schema(tags=["application"])
class ApplicationViewSet(BaseViewSet):
    filterset_class = ApplicationFilterSet
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["id"]

    serializer_class_map = {
        "list": ApplicationSerializer,
        "create": CreateApplicationSerializer,
        "retrieve": ApplicationSerializer,
        "update": UpdateApplicationSerializer,
        "approve": ApproveApplicationSerializer,
        "reject": RejectApplicationSerializer
    }

    def get_queryset(self):
        queryset = Application.objects.select_related('job_open')
        if self.request.user.is_anonymous:
            return queryset

        return queryset

    @extend_schema(responses=ApplicationSerializer(many=True))
    def list(self, request):
        return self._list()

    @extend_schema(
        responses=CreateApplicationSerializer.Meta.response_serializer_class)
    def create(self, request):
        obj = self._create()
        return obj

    @extend_schema(
        responses=UpdateApplicationSerializer.Meta.response_serializer_class)
    def update(self, request, pk=None):
        try:
            application = ApplicationSerializer.objects.filter(
                pk=pk
            ).get()
        except Laboratory.DoesNotExist:
            raise Http404

        return self._update(instance=application)

    @extend_schema(responses=ApplicationSerializer)
    def retrieve(self, request, pk=None):
        try:
            application = JobOpenSerializer.objects.filter(
                pk=pk
            ).get()
        except JobOpenSerializer.DoesNotExist:
            raise Http404

        return self._retrieve(application)

    @extend_schema(responses=ApproveApplicationSerializer)
    @action(methods=["post"], detail=True)
    def approve(self, request, pk=None):
        try:
            application = Application.objects.filter(
                pk=pk
            ).get()
        except Application.DoesNotExist:
            raise Http404

        return self._update(instance=application)

    @extend_schema(responses=RejectApplicationSerializer)
    @action(methods=["post"], detail=True)
    def reject(self, request, pk=None):
        try:
            application = Application.objects.filter(
                pk=pk
            ).get()
        except Application.DoesNotExist:
            raise Http404

        return self._update(instance=application)
