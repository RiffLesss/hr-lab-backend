import random
import uuid
from typing import List

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField

from hrlab import settings
from hrlab.user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    class Meta:
        ordering = ['id', ]
        db_table = "user"

    created_at = models.DateTimeField(default=timezone.now,
                                      verbose_name="Дата добавления")

    USERNAME_FIELD = "login"

    login = models.CharField(max_length=25, unique=True)

    first_name = models.CharField(max_length=600)

    last_name = models.CharField(max_length=600)

    middle_name = models.CharField(max_length=600)

    education = models.CharField(max_length=600)

    work_experience = models.CharField(max_length=600, blank=True, null=True)

    project_experience = models.CharField(max_length=600, blank=True, null=True)

    cv_link = models.CharField(max_length=600)

    email = models.EmailField(unique=True)

    phone = PhoneNumberField()

    is_staff = models.BooleanField(
        default=False,
        help_text="Indicates whether the user can log into this admin site.",
    )

    class Role(models.TextChoices):
        ADMIN = "Administrator"
        LAB = "Lab_Employee"
        USER = "User"

    role = models.CharField(max_length=20,
                            choices=Role.choices,
                            default=Role.USER)

    is_deleted = models.BooleanField(default=False, blank=True)

    def has_method_permission(self, method_permission: str) -> bool:
        method_permission_values = [m_p.value for m_p in self.method_permissions]
        # ?? super user permission value ??
        return method_permission in method_permission_values

    # permissions
    @property
    def method_permissions(self) -> List['MethodPermission']:
        method_permissions = set()
        method_permissions.update(self.user_method_permissions.all())
        return list(method_permissions)

    @property
    def view_permissions(self) -> List['ViewPermission']:
        view_permissions = set()
        view_permissions.update(self.user_view_permissions.all())
        return list(view_permissions)


class MethodPermission(models.Model):
    class Meta:
        db_table = "method_permission"

    value = models.CharField(max_length=120, default="*")

    users = models.ManyToManyField(User, related_name="user_method_permissions")


class ViewPermission(models.Model):
    class Meta:
        db_table = "view_permission"

    value = models.CharField(max_length=120, default="*")

    users = models.ManyToManyField(User, related_name="user_view_permissions")