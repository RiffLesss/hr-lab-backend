# Generated by Django 5.0.4 on 2024-05-23 10:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('is_archived', models.BooleanField(blank=True, default=False)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='manager_laboratories', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер')),
            ],
            options={
                'db_table': 'laboratory',
            },
        ),
    ]
