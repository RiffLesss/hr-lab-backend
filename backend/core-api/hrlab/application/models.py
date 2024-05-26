from django.db import models

from hrlab.jobopen.models import JobOpen
from hrlab.project.models import Project
from hrlab.user.models import User


class Application(models.Model):
    objects = models.Manager()

    class Meta:
        # ordering = ['created_at', ]
        db_table = "application"

    user = models.ForeignKey(User,
                                on_delete=models.DO_NOTHING,
                                verbose_name="Пользователь",
                                blank=True, null=True,
                                related_name="jobs")

    message = models.CharField(max_length=2000)

    class Status(models.TextChoices):
        NEW = "NEW"
        APPROVED = "APPROVED"
        REJECTED = "REJECTED"

    status = models.CharField(max_length=20,
                              choices=Status.choices,
                              default=Status.NEW)

    job_open = models.ForeignKey(JobOpen,
                                on_delete=models.DO_NOTHING,
                                verbose_name="Вакансия",
                                blank=True, null=True,
                                related_name="applied_jobs")

    is_deleted = models.BooleanField(default=False, blank=True)

    is_archived = models.BooleanField(default=False, blank=True)