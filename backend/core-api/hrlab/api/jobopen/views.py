from django.http import Http404
from drf_spectacular.utils import extend_schema
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

from contrib.drf.viewsets import BaseViewSet
from hrlab.api.jobopen.serializers import JobOpenSerializer, CreateJobOpenSerializer, UpdateJobOpenSerializer
from hrlab.jobopen.models import JobOpen
from hrlab.laboratory.models import Laboratory


class JobOpenFilterSet(filters.FilterSet):
    class Meta:
        model = JobOpen
        fields = {
            "name": ['exact'],
            "is_deleted": ['exact'],
            "is_archived": ['exact'],
        }


@extend_schema(tags=["job_open"])
class JobOpenViewSet(BaseViewSet):
    filterset_class = JobOpenFilterSet
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["id"]

    serializer_class_map = {
        "list": JobOpenSerializer,
        "create": CreateJobOpenSerializer,
        "retrieve": JobOpenSerializer,
        "update": UpdateJobOpenSerializer
    }

    def get_queryset(self):
        queryset = JobOpen.objects.select_related('project')
        if self.request.user.is_anonymous:
            return queryset

        return queryset

    @extend_schema(responses=JobOpenSerializer(many=True))
    def list(self, request):
        return self._list()

    @extend_schema(
        responses=CreateJobOpenSerializer.Meta.response_serializer_class)
    def create(self, request):
        obj = self._create()
        return obj

    @extend_schema(
        responses=UpdateJobOpenSerializer.Meta.response_serializer_class)
    def update(self, request, pk=None):
        try:
            job_open = JobOpenSerializer.objects.filter(
                pk=pk
            ).get()
        except Laboratory.DoesNotExist:
            raise Http404

        return self._update(instance=job_open)

    @extend_schema(responses=JobOpenSerializer)
    def retrieve(self, request, pk=None):
        try:
            job_open = JobOpenSerializer.objects.filter(
                pk=pk
            ).get()
        except JobOpenSerializer.DoesNotExist:
            raise Http404

        return self._retrieve(job_open)
