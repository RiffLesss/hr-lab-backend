from django.db import models

from hrlab.project.models import Project


class JobOpen(models.Model):
    objects = models.Manager()

    class Meta:
        # ordering = ['created_at', ]
        db_table = "job_open"

    name = models.CharField(max_length=200)

    requirements = models.CharField(max_length=2000)

    salary = models.IntegerField()

    project = models.ForeignKey(Project,
                                on_delete=models.DO_NOTHING,
                                verbose_name="Проект",
                                blank=True, null=True,
                                related_name="jobs")

    is_deleted = models.BooleanField(default=False, blank=True)

    is_archived = models.BooleanField(default=False, blank=True)
