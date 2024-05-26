from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from hrlab.api.application.views import ApplicationViewSet
from hrlab.api.auth.views import AuthViewSet
from hrlab.api.jobopen.views import JobOpenViewSet
from hrlab.api.laboratory.views import LaboratoryViewSet
from hrlab.api.profile.views import ProfileViewSet
from hrlab.api.project.views import ProjectViewSet

router = DefaultRouter()

router.register(r"v1/auth", AuthViewSet, basename="auth")
router.register(r"v1/profile", ProfileViewSet, basename="profile")
router.register(r"v1/project", ProjectViewSet, basename="project")
router.register(r"v1/laboratory", LaboratoryViewSet, basename="laboratory")
router.register(r"v1/job_open", JobOpenViewSet, basename="job_open")
router.register(r"v1/application", ApplicationViewSet, basename="application")

urlpatterns = [
    path("v1/hr_lab/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
