from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework import permissions, status
from rest_framework.decorators import action

from contrib.drf.viewsets import BaseViewSet
from hrlab.api.auth.serializers import SignInSerializer, RegisterSerializer
from django.utils.decorators import method_decorator


@extend_schema(tags=["hr_lab"])
class AuthViewSet(BaseViewSet):

    serializer_class_map = {
        "sign_in": SignInSerializer,
        "register": RegisterSerializer
                            }

    @extend_schema(responses=SignInSerializer.Meta.response_serializer_class)
    @action(["post"], detail=False, permission_classes=(permissions.AllowAny,))
    def sign_in(self, request):
        request.data._mutable = True
        return self._create(success_status=status.HTTP_200_OK)

    @action(["post"], detail=False, permission_classes=(permissions.AllowAny,))
    def register(self, request):
        request.data._mutable = True
        request.data['login'] = request.data['login'].lower()
        obj = self._create()
        return obj
