from django.db import models

from hrlab.user.models import User


class Laboratory(models.Model):
    objects = models.Manager()

    class Meta:
        # ordering = ['created_at', ]
        db_table = "laboratory"

    name = models.CharField(max_length=200)

    link = models.CharField(max_length=200)

    manager = models.ForeignKey(User,
                                on_delete=models.DO_NOTHING,
                                verbose_name="Менеджер",
                                blank=True, null=True,
                                related_name="manager_laboratories")

    is_deleted = models.BooleanField(default=False, blank=True)

    is_archived = models.BooleanField(default=False, blank=True)
