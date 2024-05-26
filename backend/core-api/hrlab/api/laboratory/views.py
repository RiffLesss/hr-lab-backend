from django.http import Http404
from drf_spectacular.utils import extend_schema
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

from contrib.drf.viewsets import BaseViewSet
from hrlab.api.laboratory.serializers import LaboratorySerializer, CreateLaboratorySerializer, \
    UpdateLaboratorySerializer
from hrlab.laboratory.models import Laboratory


class LaboratoryFilterSet(filters.FilterSet):
    class Meta:
        model = Laboratory
        fields = {
            "name": ['icontains'],
            "is_deleted": ['exact'],
            "is_archived": ['exact'],
        }


@extend_schema(tags=["laboratory"])
class LaboratoryViewSet(BaseViewSet):
    filterset_class = LaboratoryFilterSet
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["id"]

    serializer_class_map = {
        "list": LaboratorySerializer,
        "create": CreateLaboratorySerializer,
        "retrieve": LaboratorySerializer,
        "update": UpdateLaboratorySerializer
    }

    def get_queryset(self):
        queryset = Laboratory.objects.select_related('manager')
        if self.request.user.is_anonymous:
            return queryset

        return queryset

    @extend_schema(responses=LaboratorySerializer(many=True))
    def list(self, request):
        return self._list()

    @extend_schema(
        responses=CreateLaboratorySerializer.Meta.response_serializer_class)
    def create(self, request):
        obj = self._create()
        return obj

    @extend_schema(
        responses=UpdateLaboratorySerializer.Meta.response_serializer_class)
    def update(self, request, pk=None):
        try:
            laboratory = LaboratorySerializer.objects.filter(
                pk=pk
            ).get()
        except Laboratory.DoesNotExist:
            raise Http404

        return self._update(instance=laboratory)

    @extend_schema(responses=LaboratorySerializer)
    def retrieve(self, request, pk=None):
        try:
            laboratory = LaboratorySerializer.objects.filter(
                pk=pk
            ).get()
        except LaboratorySerializer.DoesNotExist:
            raise Http404

        return self._retrieve(laboratory)
