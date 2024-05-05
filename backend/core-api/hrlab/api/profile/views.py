from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action

from contrib.drf.viewsets import BaseViewSet
from hrlab.api.profile.serializers import SelfProfileSerializer


@extend_schema(tags=["profile"])
class ProfileViewSet(BaseViewSet):

    serializer_class_map = {
        "self": SelfProfileSerializer,
    }

    @action(methods=["get"], detail=False)
    def self(self, request):
        return self._retrieve(request.user)
