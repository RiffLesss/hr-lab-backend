from django.db import models

from hrlab.laboratory.models import Laboratory
from hrlab.user.models import User


class Project(models.Model):
    objects = models.Manager()

    class Meta:
        # ordering = ['created_at', ]
        db_table = "project"

    name = models.CharField(max_length=20)

    budget = models.IntegerField()

    manager = models.ForeignKey(User,
                                 on_delete=models.DO_NOTHING,
                                 verbose_name="Менеджер",
                                 blank=True, null=True,
                                 related_name="manager_projects")

    project_deadline = models.DateField()

    application_deadline = models.DateField()

    laboratory = models.ForeignKey(Laboratory,
                                 on_delete=models.DO_NOTHING,
                                 verbose_name="Лаборатория",
                                 blank=True, null=True,
                                 related_name="laboratory_projects")

    is_deleted = models.BooleanField(default=False, blank=True)

    is_archived = models.BooleanField(default=False, blank=True)