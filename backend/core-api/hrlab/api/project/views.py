from django.http import Http404
from drf_spectacular.utils import extend_schema
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

from contrib.drf.viewsets import BaseViewSet
from hrlab.api.project.serializers import ProjectSerializer, CreateProjectSerializer, UpdateProjectSerializer
from hrlab.project.models import Project


class ProjectFilterSet(filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            "laboratory": ['exact'],
            "name": ['icontains'],
            "is_deleted": ['exact'],
            "is_archived": ['exact'],
        }


@extend_schema(tags=["project"])
class ProjectViewSet(BaseViewSet):
    filterset_class = ProjectFilterSet
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["id"]

    serializer_class_map = {
        "list": ProjectSerializer,
        "create": CreateProjectSerializer,
        "retrieve": ProjectSerializer,
        "update": UpdateProjectSerializer
    }

    def get_queryset(self):
        queryset = Project.objects.select_related('manager', 'laboratory').prefetch_related('jobs', 'applications')
        if self.request.user.is_anonymous:
            return queryset

        return queryset

    @extend_schema(responses=ProjectSerializer(many=True))
    def list(self, request):
        return self._list()

    @extend_schema(
        responses=CreateProjectSerializer.Meta.response_serializer_class)
    def create(self, request):
        obj = self._create()
        return obj

    @extend_schema(
        responses=UpdateProjectSerializer.Meta.response_serializer_class)
    def update(self, request, pk=None):
        try:
            project = ProjectSerializer.objects.filter(
                pk=pk
            ).get()
        except Project.DoesNotExist:
            raise Http404

        return self._update(instance=project)

    @extend_schema(responses=ProjectSerializer)
    def retrieve(self, request, pk=None):
        try:
            project = ProjectSerializer.objects.filter(
                pk=pk
            ).get()
        except ProjectSerializer.DoesNotExist:
            raise Http404

        return self._retrieve(project)