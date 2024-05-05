from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from hrlab.api.auth.views import AuthViewSet
from hrlab.api.profile.views import ProfileViewSet
router = DefaultRouter()

router.register(r"v1/auth", AuthViewSet, basename="auth")
router.register(r"v1/profile", ProfileViewSet, basename="profile")


urlpatterns = [
    path("v1/hr_lab/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
